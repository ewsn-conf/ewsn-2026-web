#!/usr/bin/env python3

import argparse
import pandas as pd

from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import DoubleQuotedScalarString as DQ


def parse_ods(input_file, entries, title_map):
    if input_file.endswith("odf"):
        df = pd.read_excel(input_file, engine="odf")
    elif input_file.endswith("csv"):
        df = pd.read_csv(input_file)

    df.columns = [c.strip() for c in df.columns]

    required_columns = {
        "title",
        "given_name",
        "family_name",
        "affiliation",
    }

    missing = required_columns - set(df.columns)
    if missing:
        raise ValueError(
            f"{input_file}: missing required columns: {', '.join(sorted(missing))}"
        )

    for _, row in df.iterrows():
        title_text = str(row["title"]).strip()

        author = {
            "name": DQ(
                f"{str(row['given_name']).strip()} "
                f"{str(row['family_name']).strip()}"
            ),
            "affiliation": DQ(str(row["affiliation"]).strip()),
        }

        if title_text not in title_map:
            entry = {
                "title": DQ(title_text),
                "authors": [],
            }
            entries.append(entry)
            title_map[title_text] = entry

        title_map[title_text]["authors"].append(author)


def write_yaml(data, output_file):
    yaml = YAML()
    yaml.default_flow_style = False

    yaml.indent(mapping=2, sequence=4, offset=2)

    with open(output_file, "w", encoding="utf-8") as f:
        yaml.dump(data, f)


def main():
    parser = argparse.ArgumentParser(
        description="Convert list of accepted papers to YAML."
    )

    parser.add_argument(
        "inputs",
        nargs="+",
        help="One or more input .ods / .csv files",
    )

    parser.add_argument(
        "output",
        help="Output .yml file",
    )

    args = parser.parse_args()

    entries = []
    title_map = {}

    for input_file in args.inputs:
        parse_ods(input_file, entries, title_map)

    # Sort papers alphabetically (case-insensitive)
    entries.sort(key=lambda e: e["title"].casefold())

    data = {
        "entries": entries
    }

    write_yaml(data, args.output)

    print(f"Wrote {len(entries)} entries to {args.output}")


if __name__ == "__main__":
    main()
