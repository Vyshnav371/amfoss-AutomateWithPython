import ezsheets
ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
print("File Loaded")
sheet=ss[0]
n=sheet.rowCount
for i in range(2,n+1):
    if int(ss[0].getRow(i)[0])*int(ss[0].getRow(i)[1])==int(ss[0].getRow(i)[2]):
        continue
    else:
        print("The row "+str(i)+" has a mistake")
        print("it is given that")
        print(ss[0].getRow(i)[0]+'*'+ss[0].getRow(i)[1]+'='+ss[0].getRow(i)[2])
        break
