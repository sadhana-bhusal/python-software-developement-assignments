import csv #importing csv package
from openpyxl import Workbook #importing openpyxl package
wb = Workbook() #creating a workbook
ws = wb.active #move to the active worksheet
f = open('full_city_list.txt', 'r') #opening up the text file
data = csv.reader(f, delimiter=';') #iterate over the lines of file
for row in data:
    ws.append(row)
wb.save('full_city_list.xlsx')
