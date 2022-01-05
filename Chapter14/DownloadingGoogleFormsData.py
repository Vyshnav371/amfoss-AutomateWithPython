import ezsheets
ss = ezsheets.Spreadsheet('12alNzs8dhgKhQDhP4ENkLg-ygusfBibWKeW8gkZyPNA')
sheet=ss[0]
l=sheet.getColumn(3)
for i in range(len(l)):
    if l[i]=='' and l[i+1]=='':
        l=l[1:i]
        break
file=open('Email.txt','a')
for i in l:
    file.write(i+'\n')
file.close()
