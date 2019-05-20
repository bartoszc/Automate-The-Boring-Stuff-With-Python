from openpyxl.styles import Font, NamedStyle
import openpyxl
from openpyxl.workbook import Workbook

# Here’s an example that creates a new workbook and sets cell A1 to have a 24-point, italicized font.
wb = Workbook()
sheet = wb.active
a1 = sheet['A1']
a1.font = Font(size=24, italic=True)
sheet['A1'] = 'Hello World'
wb.save('styled.xlsx')

sheet = wb.active
a1 = sheet['A1']
a1.font = Font(name='Times New Roman', bold=True)
sheet['A1'] = 'Bold Times New Roman'

b3 = sheet['B3']
b3.font = Font(size=24, italic=True)
sheet['B3'] = '24 pt Italic'
wb.save('styles.xlsx')
