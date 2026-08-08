# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:46:45 2026

@author: leojf
"""
from src.pdf_utils import get_pdf_fields

#define the path of template PDF
pdf_path = "input_data/ao440.pdf"

# Read "form fields" of template PDF
result = get_pdf_fields(pdf_path)

#Print results
if isinstance(result, dict):
    for field_name, field_data in result.items():
        print(f"Field Name: {field_name}")
        print(f"Field Data: {field_data}\n" + "-"*10)
else:
    print(result)

## Go through the form field names that were printed out and 
## manually map them to columns in your excel sheet
input("Press [Enter] after updating your Excel sheet to continue")

### Load data from excel sheet
from src.excel_utils import load_defendant_data
df = load_defendant_data("input_data/Defendant_Info.xlsx")

## Loop through each row of df, converting row to dictionary
for index, row in df.iterrows():
    field_mapping = row.to_dict()
    print(f"Processing row {index + 1} for: {row['Defendant']}")   
    
    ##Defines a unique output filename for this specific row
    defendant_name = str(row['Defendant']).replace(" ", "_")
    casenumber = str(row["Civil action number"]).replace("-", "")
    output_pdf_path = f"output_data/ao440_{casenumber}_{defendant_name}.pdf"
    
    from src.pdf_utils import fill_pdf_form
    fill_pdf_form(
        input_pdf_path="input_data/ao440.pdf", 
        output_pdf_path=output_pdf_path,
        data_dict=field_mapping
    )
 
 
    
    