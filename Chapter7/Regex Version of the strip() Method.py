import re
def strip(txt,n='0'):
    if n=='0':
        space=re.compile(r'\w+')
        new=space.search(txt)
        q=new.group()
        print(q)
    else:
        delete=re.compile(n)
        new=delete.sub('',txt)
        print(new)
print("Enter a string")
a=input()
print("enter an arguement, 0 if none")
ar=input()
strip(a,ar)
