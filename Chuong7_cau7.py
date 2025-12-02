import xlsxwriter # type: ignore
from pathlib import Path

workbook  = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet('Sheet1')

worksheet.set_column('A:A', 5)
worksheet.set_column('B:B', 15)
worksheet.set_column('C:C', 20)
worksheet.set_column('D:D', 15)
worksheet.set_column('E:E', 15)

bold   = workbook.add_format({'bold': True})
center = workbook.add_format({'align': 'center'})
money  = workbook.add_format({'num_format': '#,##0', 'align': 'right'})


worksheet.write('A1', 'STT', bold)
worksheet.write('B1', 'MÃ SẢN PHẨM', bold)
worksheet.write('C1', 'TÊN SẢN PHẨM', bold)
worksheet.write('D1', 'SỐ LƯỢNG', bold)
worksheet.write('E1', 'ĐƠN GIÁ', bold)


rows = [
    [1, 'SP1', 'Coca',  15, 15000],
    [2, 'SP2', 'Pepsi', 20, 18000],
]

r = 1
for stt, ma, ten, sl, dg in rows:
    worksheet.write_number(r, 0, stt, center)
    worksheet.write(r, 1, ma)
    worksheet.write(r, 2, ten)
    worksheet.write_number(r, 3, sl, center)
    worksheet.write_number(r, 4, dg, money)
    r += 1

logo_path = Path('logo_UEL.png')
if logo_path.exists():
    worksheet.insert_image('B5', str(logo_path), {'x_scale': 0.8, 'y_scale': 0.8})

workbook.close()
print('Đã tạo demo.xlsx xong!')