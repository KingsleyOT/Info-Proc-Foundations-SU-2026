
##Imports an excel sheet and creates a DataFrame
import pandas as pd

def load_defendant_data(excel_path="data/Defendant_Info.xlsx"):
    df = pd.read_excel(excel_path)
    return df