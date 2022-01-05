import requests,bs4
a=input('Enter url of Website: ')
res=requests.get(a)
linkcheck= bs4.BeautifulSoup(res.text, 'html.parser')
links=linkcheck.findAll('a')
l,l1,l2=[],[],[]
for i in links:
    l.append(i.get('href'))
for i in l:
    new=requests.get(a)
    if new.status_code==404:
        l1.append(i)
    else:
        l2.append(i)
'''if len(l2)!=0:
    print("the following pages are found")
    for i in l2:
        print(i)'''
if len(l1)!=0:
    print("the following pages are not found")
for i in l1:
    print(i)

        
    
    
#https://automatetheboringstuff.com/
