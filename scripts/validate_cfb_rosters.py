
#!/usr/bin/env python3
import sys, csv, json, re, pathlib
try:
    from jsonschema import validate, ValidationError, Draft202012Validator
except Exception:
    validate = None
    ValidationError = Exception
    Draft202012Validator = None

SCHEMA_FILE = "StatLock_v2_2_CFB_Rosters.schema.json"

PRIMARY_KEYS = ("team_name","player_name","pos","source_url")

def read_schema(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def iter_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line: 
                continue
            yield json.loads(line)

def iter_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row

def validate_records(records, schema):
    errs = []
    seen = set()
    # Regex sanity checks
    http_re = re.compile(r"^https?://", re.I)
    height_re = re.compile(r"^\d{3,4}$")  # e.g., 5110 or 6020

    if validate and Draft202012Validator:
        validator = Draft202012Validator(schema)
        for i, rec in enumerate(records, 1):
            # JSON Schema validation
            for error in validator.iter_errors(rec):
                errs.append((i, f"schema: {error.message}"))
            # PK uniqueness
            key = tuple(rec.get(k, "") for k in PRIMARY_KEYS)
            if key in seen:
                errs.append((i, f"duplicate primary key {key}"))
            else:
                seen.add(key)
            # Extra checks
            if rec.get("source_url") and not http_re.match(str(rec["source_url"])):
                errs.append((i, "source_url not http(s)"))
            ht = str(rec.get("height","")).strip()
            if ht and not height_re.match(ht):
                # warn only
                errs.append((i, f"warn: unexpected height format '{ht}' (expected scouts-style like 6020)"))
    else:
        for i, rec in enumerate(records, 1):
            # minimal checks without jsonschema
            for field in ("team_name","conference","player_name","pos","source_url"):
                if not rec.get(field):
                    errs.append((i, f"missing required field '{field}'"))
            key = tuple(rec.get(k, "") for k in PRIMARY_KEYS)
            if key in seen:
                errs.append((i, f"duplicate primary key {key}"))
            else:
                seen.add(key)
    return errs

def main():
    if len(sys.argv) < 2:
        print("Usage: validate_cfb_rosters.py <cfb_rosters_ourlads_fbs.csv|.jsonl>")
        sys.exit(2)
    inp = pathlib.Path(sys.argv[1])
    schema_path = pathlib.Path(SCHEMA_FILE)
    if not schema_path.exists():
        print(f"ERROR: schema file not found: {schema_path}")
        sys.exit(1)
    schema = read_schema(schema_path)
    # choose reader
    if inp.suffix.lower() == ".jsonl":
        records = list(iter_jsonl(inp))
    else:
        records = list(iter_csv(inp))
    errs = validate_records(records, schema)
    if not errs:
        print(f"OK: {len(records)} records validated")
        sys.exit(0)
    print(f"Found {len(errs)} issues:")
    for i,(row, msg) in enumerate(errs[:200], 1):
        print(f"{i:03d}. row {row}: {msg}")
    if len(errs) > 200:
        print(f"... plus {len(errs)-200} more")
    sys.exit(1 if errs else 0)

if __name__ == "__main__":
    main()
