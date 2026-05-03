import yaml, json, shutil, re
from pathlib import Path

files_to_copy = [
    ("README.md",       "docs/home.md"),
    ("CRITERIA.md",     "docs/criteria.md"),
    ("CONTRIBUTING.md", "docs/contributing.md"),
    ("CHANGELOG.md",    "docs/changelog.md"),
]
link_rewrites = {
    # internal
    r"\bCRITERIA\.md\b":          "criteria.md",
    r"\bCONTRIBUTING\.md\b":      "contributing.md",
    r"\bCHANGELOG\.md\b":         "changelog.md",
    r"\bREADME\.md\b":            "home.md",

    # ratings index
    r"https://makovanilya\.github\.io/VGPR/#/ratings/": "ratings.md",
    r"ratings/_index\.md":        "ratings.md",

    # license
    r"\]\(LICENSE\)":             "](https://creativecommons.org/publicdomain/zero/1.0/)",
    r"https://makovanilya\.github\.io/VGPR/#/LICENSE": "https://creativecommons.org/publicdomain/zero/1.0/",
    r"http://LICENSE":            "https://creativecommons.org/publicdomain/zero/1.0/",

    # main
    r"http://CONTRIBUTING\.md":   "contributing.md",
    r"http://CRITERIA\.md":       "criteria.md",
    r"http://CHANGELOG\.md":      "changelog.md",
    r"http://README\.md":         "home.md",

    # github shortcuts
    r"\]\(issues\)":              "](https://github.com/makovanilya/VGPR/issues)",
    r"\]\(\.\./\.\./issues\)":    "](https://github.com/makovanilya/VGPR/issues)",
    r"\]\(discussions\)":         "](https://github.com/makovanilya/VGPR/discussions)",
    r"\]\(\.\./\.\./discussions\)": "](https://github.com/makovanilya/VGPR/discussions)",
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

github_rows = ["| Game | Rating | Tags | EoL Date |",
               "|------|--------|------|----------|"]
docs_rows   = ["| Game | Rating | Tags | EoL Date |",
               "|------|--------|------|----------|"]

REPO_BLOB = "https://github.com/makovanilya/VGPR/blob/main/ratings"

for r in ratings:
    tags = ", ".join(r.get("tags", []))
    github_link = f"[{r['game']}](./{r['file']})"
    docs_link   = f"[{r['game']}]({REPO_BLOB}/{r['file']})"
    github_rows.append(f"| {github_link} | {r['rating']} | {tags} | {r.get('eol_date','')} |")
    docs_rows.append(f"| {docs_link} | {r['rating']} | {tags} | {r.get('eol_date','')} |")

Path("ratings/_index.md").write_text("\n".join(github_rows))
Path("docs/ratings.md").write_text("\n".join(docs_rows))
print(f"Indexed {len(ratings)} ratings.")
