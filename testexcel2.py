#coding:utf-8
import xlsxwriter as excel

excel = excel.Workbook('demo6.xlsx')
format1 = excel.add_format({'bold': True, 'font_color': 'blue'})

sheet = excel.add_worksheet('heloo123')
#sheet.set_column('A:A',120)

chart = excel.add_chart({'type':'column'})
data = [
    [1, 2, 3, 4, 5],
    [2, 4, 6, 8, 10],
    [3, 6, 9, 12, 15],
]

sheet.write_column('A1', data[0])
sheet.write_column('B1', data[1])
sheet.write_column('C1', data[2])
chart.add_series({'values': '=heloo123!$A$1:$A$5','categories':'=heloo123!$A$1:$A$5'})
chart.add_series({'values': '=heloo123!$B$1:$B$5'})
chart.add_series({'values': '=heloo123!$C$1:$C$5'})

sheet.insert_chart('A7',chart)
#worksheet.insert_chart('A7', chart)
#sheet.write('A1',u'你好号好号')

#b=1
#with open('vios7.log') as f:
#    for i in f:
        #print i.decode('utf-8')
#        sheet.write(b,0,i.decode('utf-8'),format1)
#        b=b+1
excel.close()
