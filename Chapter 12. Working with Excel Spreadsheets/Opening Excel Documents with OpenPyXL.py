import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
print(type(wb))  # <class 'openpyxl.workbook.workbook.Workbook'>
