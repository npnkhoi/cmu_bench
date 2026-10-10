"""Validate data/benchmarks.yaml and regenerate the benchmark table in README.md.

The table is written between the AUTOGEN markers in README.md; everything else in
the README is hand-written and left untouched. Exits non-zero on invalid entries.

Usage:
    conda run -n ds python scripts/build_readme.py
"""
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "benchmarks.yaml"
README = ROOT / "README.md"
START, END = "<!-- AUTOGEN:START -->", "<!-- AUTOGEN:END -->"

FIELDS = ["name", "year", "languages", "tasks", "paper", "dataset_url", "access", "size"]
ACCESS = {"public", "form", "on-request", "unavailable"}
ACCESS_LABEL = {"public": "Link", "form": "Form", "on-request": "On request"}


def validate(entries):
    errors, names = [], set()
    for i, e in enumerate(entries):
        tag = e.get("name", f"entry #{i}")
        if set(e) != set(FIELDS):
            errors.append(f"{tag}: fields must be exactly {FIELDS}")
            continue
        if e["name"] in names:
            errors.append(f"{tag}: duplicate name")
        names.add(e["name"])
        if e["access"] not in ACCESS:
            errors.append(f"{tag}: access must be one of {sorted(ACCESS)}")
        if (e["dataset_url"] is None) != (e["access"] == "unavailable"):
            errors.append(f"{tag}: dataset_url must be null iff access is 'unavailable'")
        if not isinstance(e["tasks"], list) or not e["tasks"]:
            errors.append(f"{tag}: tasks must be a non-empty list")
    return errors


def render(entries):
    cell = lambda s: str(s).replace("|", "\\|")
    rows = [
        "| Name | Year | Languages | Tasks | Paper | Data | Size |",
        "|---|---|---|---|---|---|---:|",
    ]
    for e in sorted(entries, key=lambda e: (-e["year"], e["name"].strip("“”\"").lower())):
        data = (f"[{ACCESS_LABEL[e['access']]}]({e['dataset_url']})"
                if e["dataset_url"] else "Unavailable")
        rows.append("| " + " | ".join([
            cell(e["name"]),
            str(e["year"]),
            cell(", ".join(e["languages"]) or "?"),
            cell(", ".join(e["tasks"])),
            f"[Paper]({e['paper']})",
            data,
            f"{e['size']:,}" if e["size"] is not None else "?",
        ]) + " |")
    n_langs = len({l for e in entries for l in e["languages"]})
    summary = f"**{len(entries)} datasets** across **{n_langs} languages**.\n\n"
    return summary + "\n".join(rows)


def main():
    entries = yaml.safe_load(DATA.read_text())
    errors = validate(entries)
    if errors:
        print("Invalid data/benchmarks.yaml:\n" + "\n".join(f"  - {e}" for e in errors))
        sys.exit(1)
    text = README.read_text()
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    README.write_text(f"{head}{START}\n{render(entries)}\n{END}{tail}")
    print(f"README.md updated with {len(entries)} datasets")


if __name__ == "__main__":
    main()
