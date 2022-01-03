from pathlib import Path
import re,shutil,os
a=input('enter path')
p=Path(a)
b=input('enter Extension to sort: ')
c=input('enter prefix of file to sort')
if b[0]=='.':
    b=b[1:]
l=list(p.glob('*.'+b))
s=''
l1=[]
m=len(c)
for i in l:
    if i.stem[:m]==c:
        l1.append(i.stem)
if len(l1)==0:
    print("Some input is wrong")
    os.exit()
l2=l1.copy()
n=len(l1[0])-m
for i in range(len(l1)):
    l1[i]=l1[i][m:]
for i in range(len(l1)):
    l1[i]=int(l1[0])+i
    if len(str(l1[i]))<n:
        k=n-len(str(l1[i]))
        l1[i]=(k)*'0'+str(l1[i])
    else:
        l1[i]=str(l1[i])
for i in range(len(l1)):
    l1[i]=c+l1[i]
for i in range(len(l1)):
    v=l2[i]+'.'+b
    c=l1[i]+'.'+b
    shutil.move(p/v,p/c)
print("previous names: ",*l2)
print("New names     : ",*l1)


    

