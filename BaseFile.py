import xlrd
from xlrd import open_workbook

class ExcelOperations(object):
    def __init__(self, *selected_test_case_values):
        self._selected_test_case_values=selected_test_case_values

    def __str__(self):
        return (" TestCaseid = {0}".format(self._selected_test_case_values))

workBook=open_workbook('C:/Users/rahul.mishra/Desktop/clearcare_new/Excel_Input.xlsx')
for sheet in workBook.sheets():
    if sheet.name != "RestClientData":
        continue
    numberOfRows=sheet.nrows
    numberOfColumns=sheet.ncols

    items=[]
    rows=[]
    # data processing logic
    for row in range(1,numberOfRows):
        values=[]
        for col in range(1,numberOfColumns):
            #import pdb;pdb.set_trace()
            value=(sheet.cell(row,col).value)
            try:
                value=str(int(value))

            except ValueError:
                pass
            finally:
                values.append(value)

        item=ExcelOperations(*values)
        items.append(item)

#printing the items from list
for item in items:
    print(item)
