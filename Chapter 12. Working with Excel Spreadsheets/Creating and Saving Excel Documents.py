import openpyxl
wb = openpyxl.Workbook()
print(wb.get_sheet_names())  # ['Sheet']
sheet = wb.get_active_sheet()
print(sheet.title)  # 'Sheet'
sheet.title = 'Spam Bacon Eggs Sheet'
print(wb.get_sheet_names())  # ['Spam Bacon Eggs Sheet']

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_active_sheet()
sheet.title = 'Spam Spam Spam'
wb.save('example_copy.xlsx')
