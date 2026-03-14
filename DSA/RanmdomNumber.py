import random
generated_number = random.randint(1,100)

user_number = int(input("Enter Number: "))
count = 1
while generated_number != user_number:
    # if generated_number==user_number:
    #     break
    if generated_number<user_number:
        print("Lower then to your number!")
    else:
        print("Greater then then to your number!")
    user_number = int(input("Enter Number: "))
    count += 1

print(f"You won this game in {count} attempt.")

# print(generated_number)

# ________________________________chatGPT_________________________________

# import random

# number = random.randint(1, 100)

# while True:
#     guess = int(input("Guess the number: "))
    
#     if guess > number:
#         print("Too High")
#     elif guess < number:
#         print("Too Low")
#     else:
#         print("Correct! You guessed it.")
#         break
