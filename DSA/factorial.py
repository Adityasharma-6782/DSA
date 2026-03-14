# import math as m

# num = int(input("Enter a number: "))
# factorial = m.factorial(num)

# print(f"factorial of {num} is {factorial}")


num = int(input("Enter a number: "))
def fact(num):
    if num == 1 or num == 0:
        return 1
    return num*fact(num-1)

print(f"factorial of {num} is", fact(num))