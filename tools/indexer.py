import yaml, json, shutil
from pathlib import Path

files_to_copy = [
    ("README.md",       "docs/home.md"),
    ("CRITERIA.md",     "docs/criteria.md"),
    ("CONTRIBUTION.md", "docs/contributing.md"),
    ("CHANGELOG.md",    "docs/changelog.md"),
]
for src, dst in files_to_copy:
    if Path(src).exists():
        shutil.copy(src, dst)
        print(f"Copied {src} -> {dst}")
    else:
        print(f"SKIP: {src} not found at repo root")
        
ratings = []
for f in sorted(Path("ratings").glob("*.md")):
    if f.name in ("_index.md", "_template.md"):
        continue
    text = f.read_text()
    if not text.startswith("---"):
        continue
    _, front, _ = text.split("---", 2)
    data = yaml.safe_load(front)
    data["file"] = f.name
    ratings.append(data)

Path("docs/ratings.json").write_text(json.dumps(ratings, indent=2))

rows = ["| Game | Rating | Tags | EoL Date |",
        "|------|--------|------|----------|"]
for r in ratings:
    tags = ", ".join(r.get("tags", []))
    link = f"[{r['game']}](./ratings/{r['file']})"
    rows.append(f"| {link} | {r['rating']} | {tags} | {r.get('eol_date','')} |")

Path("ratings/_index.md").write_text("\n".join(rows))
print(f"Indexed {len(ratings)} ratings.")
