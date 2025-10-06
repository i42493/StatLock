#!/usr/bin/env python3
import csv
import json
import sys
import time
import random
import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup

INPUT_CSV = "FBS_master_roster_urls.csv"
OUT_CSV = "cfb_rosters_ourlads_fbs.csv"
OUT_JSONL = "cfb_rosters_ourlads_fbs.jsonl"

HEADERS = {
    "User-Agent": "StatLock-v2.2 (+for academic research; contact owner)"
}

def clean_text(s):
    return re.sub(r"\s+", " ", s or "").strip()

def parse_team_page(html, fallback_meta):
    soup = BeautifulSoup(html, "html.parser")

    # Team meta block
    team_name = clean_text(soup.select_one("h2, h1, h3"))
    # The info lines often appear as list items near team header
    page_text = soup.get_text("\n", strip=True)

    # Try to parse structured fields
    # Example lines on page:
    #   Stadium: Bryant-Denny Stadium (100,077) | Surface: Grass
    #   Head Coach: Kalen DeBoer
    #   Offensive Schemes: Pro Spread
    #   Defensive Schemes: 4-2-5
    #   Updated: 09/29/2025 8:33PM ET
    def grab(label):
        m = re.search(rf"{label}:\s*([^\n|]+)", page_text, flags=re.IGNORECASE)
        return clean_text(m.group(1)) if m else ""

    stadium = grab("Stadium")
    surface = grab("Surface")
    head_coach = grab("Head Coach")
    off_scheme = grab("Offensive Schemes")
    def_scheme = grab("Defensive Schemes")
    updated_at = grab("Updated")

    # Player table
    # We look for the "Active Players" block; then rows with fields
    # Typically the header line contains: "Player # Pos. HT WT Class High School Hometown"
    players = []
    # Look for the roster table by matching common column names in <table> or text blocks
    # We'll iterate over tables and choose the one containing "Player" and "Pos."
    tables = soup.find_all("table")
    target = None
    for t in tables:
        txt = clean_text(t.get_text(" "))
        if "Player" in txt and "Pos" in txt and ("Class" in txt or "Hometown" in txt):
            target = t
            break

    if target is None:
        # fallback: scan rows via <tr>
        rows = soup.find_all("tr")
    else:
        rows = target.find_all("tr")

    # Identify header to map columns
    header_map = {}
    for tr in rows:
        ths = [clean_text(th.get_text()) for th in tr.find_all(["th","td"])]
        if len(ths) >= 6 and ("Player" in " ".join(ths) and ("WT" in ths or "Weight" in " ".join(ths))):
            # Create index map
            for i, h in enumerate(ths):
                hlow = h.lower()
                if "player" in hlow:
                    header_map["player_name"] = i
                elif hlow in ("#", "no", "num", "number"):
                    header_map["jersey"] = i
                elif "pos" in hlow:
                    header_map["pos"] = i
                elif hlow in ("ht", "height"):
                    header_map["height"] = i
                elif hlow in ("wt", "weight"):
                    header_map["weight"] = i
                elif "class" in hlow:
                    header_map["class"] = i
                elif "high school" in hlow:
                    header_map["high_school"] = i
                elif "hometown" in hlow:
                    header_map["hometown"] = i
            # header found; proceed to next rows
            continue

        if header_map and len(ths) >= max(header_map.values(), default=-1) + 1:
            def getf(key):
                idx = header_map.get(key, None)
                return clean_text(ths[idx]) if idx is not None else ""

            players.append({
                "team_name": fallback_meta.get("team_name", team_name),
                "conference": fallback_meta.get("conference", ""),
                "stadium": stadium,
                "surface": surface,
                "head_coach": head_coach,
                "off_scheme": off_scheme,
                "def_scheme": def_scheme,
                "updated_at": updated_at,
                "player_name": getf("player_name"),
                "jersey": getf("jersey"),
                "pos": getf("pos"),
                "height": getf("height"),
                "weight": getf("weight"),
                "class": getf("class"),
                "high_school": getf("high_school"),
                "hometown": getf("hometown"),
                "source_url": fallback_meta.get("roster_url", ""),
            })

    return players

def fetch(url, tries=2, timeout=20):
    for i in range(tries):
        try:
            r = requests.get(url, headers=HEADERS, timeout=timeout)
            if r.status_code == 200:
                return r.text
        except requests.RequestException:
            pass
        time.sleep(1 + i)
    return None

def read_input(csv_path):
    rows = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append(r)
    return rows

def write_outputs(records, out_csv=OUT_CSV, out_jsonl=OUT_JSONL):
    # ensure consistent field order
    fields = [
        "team_name","conference","stadium","surface","head_coach",
        "off_scheme","def_scheme","updated_at",
        "player_name","jersey","pos","height","weight","class","high_school","hometown","source_url"
    ]
    # CSV
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in records:
            w.writerow({k: r.get(k, "") for k in fields})

    # JSONL
    with open(out_jsonl, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

def main():
    in_csv = Path(INPUT_CSV)
    if len(sys.argv) > 1:
        in_csv = Path(sys.argv[1])
    if not in_csv.exists():
        print(f"ERROR: input file not found: {in_csv}")
        print("Usage: python ourlads_cfb_scrape.py FBS_master_roster_urls.csv")
        sys.exit(1)

    teams = read_input(in_csv)
    all_rows = []
    for i, team in enumerate(teams, 1):
        url = team.get("roster_url", "")
        if not url:
            continue
        html = fetch(url)
        if not html:
            print(f"[{i}/{len(teams)}] FAILED: {team.get('team_name')} -> {url}")
            continue
        rows = parse_team_page(html, team)
        count = len(rows)
        all_rows.extend(rows)
        print(f"[{i}/{len(teams)}] {team.get('team_name')} — {count} players")

        # be polite
        time.sleep(random.uniform(0.8, 1.5))

    write_outputs(all_rows)
    print(f"Done. Wrote {len(all_rows)} rows to {OUT_CSV} and {OUT_JSONL}")

if __name__ == "__main__":
    main()
