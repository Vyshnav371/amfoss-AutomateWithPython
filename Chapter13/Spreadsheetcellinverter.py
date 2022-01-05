import sys,openpyxl
try:
    file=sys.argv[1]
except:
    file=input('enter file name')
wb = openpyxl.load_workbook(file)
sheet=wb.active
a,b=sheet.max_row,sheet.max_column
data=[]
for i in range(1,a+1):
    l=[]
    for j in range(1,b+1):
        l.append(sheet.cell(row=i, column=j).value)
    data.append(l)
wb = openpyxl.Workbook()
sheet=wb['Sheet']
for i in range(1,b+1):
    for j in range(1,a+1):
        sheet.cell(row=i, column=j).value=data[j-1][i-1]
wb.save("inverted.xlsx")
