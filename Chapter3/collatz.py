def collatz(number):
    if number%2==0:
        print(number//2)
        return(number//2)
    else:
        print(3 * number + 1)
        return(3 * number + 1)
while True:
    try:
        n=int(input("enter number:"))
        break
    except:
        print("enter a number not string")
        print()
while n!=1:
    n=collatz(n)
    
