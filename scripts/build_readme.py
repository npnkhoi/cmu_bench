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
AGGREGATES = ROOT / "data" / "aggregate_benchmarks.yaml"
README = ROOT / "README.md"
START, END = "<!-- AUTOGEN:START -->", "<!-- AUTOGEN:END -->"

FIELDS = ["name", "year", "languages", "tasks", "platforms", "paper", "dataset_url", "access", "size"]
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
        if not isinstance(e["platforms"], list) or any(
            not isinstance(p, str) or not p.strip() for p in e["platforms"]
        ):
            errors.append(f"{tag}: platforms must be a list of non-empty strings")
    return errors


def render_table(entries, show_languages=False):
    cell = lambda s: str(s).replace("|", "\\|")
    language_header = " Languages |" if show_languages else ""
    language_separator = "---|" if show_languages else ""
    rows = [
        f"| Name | Year |{language_header} Tasks | Platform sources | Paper | Data | Size |",
        f"|---|---|{language_separator}---|---|---|---|---:|",
    ]
    for e in sorted(entries, key=lambda e: (-e["year"], e["name"].strip("“”\"").lower())):
        data = (f"[{ACCESS_LABEL[e['access']]}]({e['dataset_url']})"
                if e["dataset_url"] else "Unavailable")
        rows.append("| " + " | ".join([
            cell(e["name"]),
            str(e["year"]),
            *([cell(", ".join(e["languages"]))] if show_languages else []),
            cell(", ".join(e["tasks"])),
            cell(", ".join(e["platforms"])) or "Not reported",
            f"[Paper]({e['paper']})",
            data,
            f"{e['size']:,}" if e["size"] is not None else "?",
        ]) + " |")
    return "\n".join(rows)


def render(entries, aggregates=()):
    n_langs = len({l for e in entries for l in e["languages"]})
    sections = [f"**{len(entries)} datasets** across **{n_langs} languages**."]
    languages = sorted({e["languages"][0] for e in entries if len(e["languages"]) == 1})
    groups = [(language, [e for e in entries if e["languages"] == [language]])
              for language in languages]
    groups.extend([
        ("Multilingual", [e for e in entries if len(e["languages"]) > 1]),
        ("Unknown language", [e for e in entries if not e["languages"]]),
    ])
    for title, group in groups:
        if group:
            sections.append(f"### {title}\n\n{render_table(group, show_languages=title == 'Multilingual')}")
    if aggregates:
        rows = [
            "### Aggregate benchmarks",
            "",
            "These benchmarks combine existing datasets and are counted separately from the datasets above.",
            "",
            "| Name | Year | Coverage | Paper | Data |",
            "|---|---|---|---|---|",
        ]
        for e in sorted(aggregates, key=lambda e: (-e["year"], e["name"].lower())):
            description = e["description"].replace("|", "\\|")
            rows.append(f"| {e['name']} | {e['year']} | {description} | "
                        f"[Paper]({e['paper']}) | [Link]({e['dataset_url']}) |")
        sections.append("\n".join(rows))
    return "\n\n".join(sections)


def main():
    entries = yaml.safe_load(DATA.read_text())
    aggregates = yaml.safe_load(AGGREGATES.read_text())
    aggregate_fields = {"name", "year", "description", "paper", "dataset_url"}
    if not isinstance(aggregates, list) or any(set(e) != aggregate_fields for e in aggregates):
        print(f"Invalid {AGGREGATES.name}: each entry must have {sorted(aggregate_fields)}")
        sys.exit(1)
    errors = validate(entries)
    if errors:
        print("Invalid data/benchmarks.yaml:\n" + "\n".join(f"  - {e}" for e in errors))
        sys.exit(1)
    text = README.read_text()
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    README.write_text(f"{head}{START}\n{render(entries, aggregates)}\n{END}{tail}")
    print(f"README.md updated with {len(entries)} datasets and {len(aggregates)} aggregate benchmarks")


if __name__ == "__main__":
    main()
