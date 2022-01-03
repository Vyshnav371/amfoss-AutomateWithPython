import random,time,pyinputplus as pyip
i=1
correct=0
while i<11:
    first=random.randint(0,9)
    second=random.randint(0,9)
    p='Q-{}: {}*{} = '.format(i,first,second)
    try:
        pyip.inputStr(p,allowRegexes=['^%s$'%(first*second)],blockRegexes=[('.*','Incorrect!')],timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correct+= 1
    i+=1
    time.sleep(1)
print("Score Obtained: {}/{}".format(correct,10))
