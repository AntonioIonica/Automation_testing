import xlsxwriter
import json


# opening the json file
with open('C:/Users/anton/PycharmProjects/Automation_testing/src/BDD_examples/test.json') as js_file:
    json_object = json.load(js_file)
    js_file.close()

# Starting a workbook with specified name of file and then adding a worksheet
workbook = xlsxwriter.Workbook('test_report.xlsx', {'strings_to_numbers':  False})
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': True})

worksheet.write('A1', 'Keys', bold)
worksheet.write('B1', 'Values', bold)


# Starting from 0 for both row(key) and col(value)
row = 1
col = 0

for row_keys, row_values in enumerate(json_object):
    for col_keys, col_values in enumerate(row_values):
        worksheet.write(row, col, col_keys)
        worksheet.write(row, col + 1, str(col_values))
        row += 1


while True:
    try:
        workbook.close()
    except xlsxwriter.exceptions.FileCreateError as e:
        decision = input("Exception caught in workbook.close(): %s\n"
                         "Please close the file if it is open in Excel.\n"
                         "Try to write file again? [Y/n]: " % e)
        if decision != 'n':
            continue

    break
