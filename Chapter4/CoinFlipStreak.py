import random
numberOfStreaks = 0
percent=0
for experimentNumber in range(10000):
    numberOfStreaks = 0
    l=[]
    s=''
    for i in range(100):
        r=random.randint(0,1)
        l.append(str(r))
    for i in l:
        s+=str(i)
    i=0
    for i in range(95):
        if s[i]==s[i+1] and s[i+1]==s[i+2] and s[i+2]==s[i+3] and s[i+3]== s[i+4] and s[i+4]==s[i+5]:
            numberOfStreaks+=1
    percent+=numberOfStreaks/100
average=percent/10000
print('Chance of streak: %s%%' % (average))
