import math as m
def primeNumber(n):
    if n<=1:
        return False
    elif n==2:
        return True
    else:
        x=abs(n/2)
        for i in range(2, int(m.sqrt(n)) + 1):
           if n % i == 0:
                return False
        
        return True

num = int(input("Enter Number: "))
if(primeNumber(num)):
    print(f"{num} is Prime Number.")
else:
    print(f"{num} is not prime Number.")