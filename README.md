# Language Explorer

## Purpose

Language Explorer helps users find published AUSTLANG records by language code, main name, or alternative name. Provides links to the original AIATSIS records and statistics about alternative-name coverage.

Intended users: Students, educators, and interested members of the public

## Features

- Search by exact code, name, or alternative name.
- Ignore capitalisation and surrounding spaces when searching.
- Display feedback for blank or unmatched searches.
- Display alternative names and an AIATSIS source link.
- View dataset statistics on the Insights page.
- Read source, licence, and limitation information on the About page.

## Installation and running

Python 3.9 or newer is required.

Open a terminal in the project folder. On macOS:

```bash
python3 -m venv .venv #Create an isolated virtual environment
source .venv/bin/activate #Activates the virtual environment
python -m pip install -r requirements.txt #automatically install a batch of Python packages
python app.py
```

Open http://127.0.0.1:5001 in a browser.

Keep the terminal running while using the website. Press Control+C to stop it. This command runs a local development server.

## Using the application

1. Open Search.
2. Enter a code, main name, or alternative name.
3. Submit the form to view the first matching record.
4. Follow the source link for further information.
5. Use the navigation links to visit Insights and About.

Search currently requires an exact match after removing surrounding spaces and ignoring capitalisation.

## Running tests

With the virtual environment active, run:

```bash
python -m unittest discover -v
```

The search tests use small artificial records. Website tests check routes and search feedback.

Latest verified result: [date, number of tests run, and outcome].

## Data source and licence

Source: Australian Institute of Aboriginal and Torres Strait Islander Studies (AIATSIS), [AUSTLANG dataset](https://data.gov.au/data/dataset/austlang-dataset-001).

Dataset licence: [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).

Original download date: 17/09/2026

The supplied dataset contains 1,204 records. Records should not be interpreted as a count of distinct languages or speakers.

The program trims whitespace, compares uppercase copies of searchable text, and separates alternative names using the `|` character. The source CSV is unchanged.

AIATSIS does not endorse this student project. The dataset licence does not automatically cover other material on linked websites.

## Analysis

The Insights page counts records with and without alternative names.

Alternative-name coverage is calculated as: records with alternative names ÷ total records × 100

An empty alternative-name field means no alternatives are supplied in that field; it does not prove that no alternative names exist.

## Project structure

- `Main.py`: search function and terminal interface.
- `app.py`: Flask routes, CSV loading, and statistics.
- `Dataset/AUSTLANG.csv`: source dataset.
- `templates/`: HTML templates.
- `static/style.css`: shared website styling.
- `test_main.py`: search tests.
- `test_app.py`: website tests.
- `AI-LOG.md`: significant AI assistance and verification.
- `ARCHITECTURE.md`: components and data flow.

## Limitations and privacy

- Search returns the first matching record when names are shared.
- Partial matching and spelling correction are not implemented.
- The dataset is a local snapshot and does not update automatically.
- The application does not generate translations or cultural explanations.
- There are no user accounts. Search terms appear in URLs and may appear in browser history or server logs; users should not enter personal information.

## Deployment

Public application URL: [add after deployment].

## Contributors and AI assistance

Contributors: [names and actual responsibilities].

AI assistance is documented in `AI-LOG.md`.