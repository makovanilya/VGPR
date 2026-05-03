import yaml, json, shutil, re
from pathlib import Path

files_to_copy = [
    ("README.md",       "docs/home.md"),
    ("CRITERIA.md",     "docs/criteria.md"),
    ("CONTRIBUTING.md", "docs/contributing.md"),
    ("CHANGELOG.md",    "docs/changelog.md"),
]
link_rewrites = {
    r"\bCRITERIA\.md\b":     "criteria.md",
    r"\bCONTRIBUTION\.md\b": "contributing.md",
    r"\bCHANGELOG\.md\b":    "changelog.md",
    r"\bREADME\.md\b":       "home.md",
    r"ratings/_index\.md":   "ratings.md",
}

for src, dst in files_to_copy:
    if Path(src).exists():
        text = Path(src).read_text(encoding="utf-8")
        for pattern, replacement in link_rewrites.items():
            text = re.sub(pattern, replacement, text)
        Path(dst).write_text(text, encoding="utf-8")
        print(f"Copied + rewrote {src} -> {dst}")
    else:
        print(f"SKIP: {src} not found")
        
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
Path("docs/ratings.md").write_text("\n".join(rows))
shutil.copy("ratings/_index.md", "docs/ratings.md")
print(f"Indexed {len(ratings)} ratings.")
