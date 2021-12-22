import re
date=re.compile(r'''(
      (\d{2})    #day
      /
      (\d{2})    #month
      /
      (\d{4}) #year
      )''',re.VERBOSE)
mo=date.findall(' my bday is on 21/06/2002 and my friend"s bday is on 03/15/2006 12/12/2006 12/09/2002 29/02/2400 28/02/2000')
l=[]
for i in mo:
    day=i[1]
    month=i[2]
    year=i[3]
    fdate=day+'/'+month+'/'+year
    e=0
    l30=['04','06','9','11']
    if  month=='02':
        if int(year)%400==0 and int(day)>28:
            e=1
        elif int(year)%4==0 and int(day)>29:
            e=1
        elif int(day)>28:
            e=1
    elif month in l30 and int(day)>30:
        e=1
    elif month not in l30 and int(day)>31:
        e=1
    if int(month)>12:
        e=1
    if e==0:
        l.append(fdate)
if len(l)==0:
    print("NO valid Dates")
else:
    print("Valid Dates")
    for i in l:
        print(i)
