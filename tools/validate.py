import sys, yaml, re
from pathlib import Path

VALID_RATINGS = {"p1","p2","p3","p4","p5","NR"}
VALID_TAGS    = {"OS","SDK","SRV","SP","ON","DRM","DLS",}
REQUIRED      = ["game","publisher","rating","tags","eol_date"]

def validate(path):
    text = Path(path).read_text()
    if not text.startswith("---"):
        return ["Missing YAML front matter"]
    _, front, _ = text.split("---", 2)
    data = yaml.safe_load(front)
    errors = []
    for field in REQUIRED:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if data.get("rating") not in VALID_RATINGS:
        errors.append(f"Invalid rating: {data.get('rating')}")
    for tag in data.get("tags", []):
        if tag not in VALID_TAGS:
            errors.append(f"Unknown tag: {tag}")
    return errors

errors = validate(sys.argv[1])
if errors:
    for e in errors: print("ERROR:", e)
    sys.exit(1)
else:
    print("OK")
