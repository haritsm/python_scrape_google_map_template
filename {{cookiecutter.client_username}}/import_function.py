# References: 
#     - https://www.journaldev.com/33306/pandas-read_excel-reading-excel-file-in-python

import pandas as pd

def import_excel(destination_path, sheet):
    df = pd.read_excel(destination_path, sheet_name = sheet)
    return df

# def import_google_sheet():
#     df = pd.read_excel (r'Path where the Excel file is stored\File name.xlsx', sheet_name='your Excel sheet name')
#     print (df)

# file_path = ("Tableau CV Information- Dulani 2.xlsx")
# sheet = 'Experience Timeline'
# data = import_excel(file_path, sheet)
# print(data)
# df = pd.DataFrame(data, columns= ['Product'])