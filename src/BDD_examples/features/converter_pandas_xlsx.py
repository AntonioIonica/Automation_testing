import pandas as pd


df_json = pd.read_json('C:/Users/anton/PycharmProjects/Automation_testing/src/BDD_examples/test.json')
df_json.to_excel('excel_reports.xlsx')
