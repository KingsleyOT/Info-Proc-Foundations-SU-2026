# Summons Generator Project


This project fills a PDF summons form using defendant data from an Excel spreadsheet. It reads the form field names from a template PDF, then maps Excel values into those fields and generates completed PDF files.

## Requirements

- `pandas`
- `pypdf`

## Setup

1. Create and activate a Python virtual environment and Install required Packages:

   pip install pandas pypdf


## Input files

Place Your template PDF and Excel files in the `input_data/` folder. These files are current saved there to demonstrate this program:

- `ao440.pdf` — the fillable PDF template.
- `Defendant_Info.xlsx` — an Excel file with a row for each defendant.


## Usage

Run the main script from the project root:

```bash
python main.py
```

The script will:

1. Read and print the PDF form field names from `input_data/ao440.pdf`.
2. Wait for you to update the Excel file to match the form field names
3. Load defendant rows from `input_data/Defendant_Info.xlsx`.
4. Generate filled PDF output files in `output_data/`.

## Output

Completed files are written to `output_data/` with names

- `ao440_<casenumber>_<defendant_name>.pdf`

## Notes

- Ensure the Excel column names match the PDF field names used by the form.
- If the PDF does not contain readable form fields, the script may return `No fields found`.
- Customize the script or field mapping if your PDF template uses different form field names.
