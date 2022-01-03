from pathlib import Path
import re
a=input('Enter path of folder to search')
p=Path(a)
l=list(p.glob('*.txt'))
r=input('Enter regex to search')
k=[]
for i in l:
    file=open(i,'r')
    s=file.read()
    regex=re.compile('.*({}).*'.format(r))
    k+=regex.findall(s)
print(k)
    
    
    
