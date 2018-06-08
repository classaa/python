#coding:utf-8
import xlsxwriter as xlsx

workbook1 = xlsx.Workbook('demo2.xlsx')
worksheet = workbook1.add_worksheet('Hello')
worksheet.set_column('A:A',10)
bold = workbook1.add_format({'bold':True})
worksheet.write('A1','Hello')
worksheet.write('A2','World',bold)
worksheet.write('B2', u'中文111112222',bold)
worksheet.write(2, 0, 32)
worksheet.write(3, 0, 35.5)
worksheet.write(4, 0, '=SUM(A3:A4)')
worksheet.insert_image('B5', 'img/python-logo.png')
workbook1.close()
