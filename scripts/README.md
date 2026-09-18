# Scripts

Utility scripts to parse relevant data for the website.

- [./parse-accepted-papers.py](./parse-accepted-papers.py): Parse .ods or .csv sheet of accepted papers into a .yml output file that can be inserted in [../content/program/accepted-papers.md](../content/program/accepted-papers.md). Expected columns: title, given_name, family_name, affiliation. One row per author.
