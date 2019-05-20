import openpyxl
wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.get_active_sheet()
sheet.freeze_panes = 'A2'
wb.save('freezeExample.xlsx')