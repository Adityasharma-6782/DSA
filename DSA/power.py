def power(n,p):
    pro = 1
    if(n==0):
       return 1
    elif n<0:
        n=abs(n)
        for i in range(p):
            pro *= n
            pro = 1/pro
    else:
        for i in range(p):
            pro *= n

    return pro

num = int(input("Enter Number: "))
pow = int(input("Enter Power: "))

print(f"Value of {num} rest to the power {pow} is", power(num,pow))