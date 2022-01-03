import random
guess = ''
def change(n):
    if n==0:
        n='tails'
    else:
        n='heads'
    return(n)
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1)# 0 is tails, 1 is heads
toss=change(toss)
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
