import re
def password(p):
    c=0
    upper=re.compile(r'[A-Z]')
    lower=re.compile(r'[a-z]')
    digit=re.compile(r'[0-9]')
    if len(p)<8:
        print("Password must be atleast 8 Characters")
        c=1
    elif upper.search(p)==None:
        print('Please add an uppercase character')
        c=1
    elif lower.search(p)==None:
        c=1
        print('Please add a Lower character')
    elif digit.search(p)==None:
        c=1
        print('Please add an digit character')
    if c==0:
        print("It is a strong Password")
p=input("enter a password")
password(p)
    
    
    
                 
