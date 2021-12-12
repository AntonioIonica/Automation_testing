import pandas as pd


df_json = pd.read_json('/test.json')
df_json.to_excel('excel_reports.xlsx')
