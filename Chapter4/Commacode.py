def idk(l):
    n=len(l)
    try:
        for i in range(n-2):
            if i!= n-1:
                print(str(l[i])+',',end=' ')
        print(str(l[-2])+' and '+str(l[-1]))
    except:
        print("empty list")
trial=eval(input())
idk(trial)
    
