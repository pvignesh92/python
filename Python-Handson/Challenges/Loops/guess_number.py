# Obtain a number randomly between 1 and 10 and use the input to guess the number

import random
num = random.randint(1,10)
guess_num = 0
counter = 0

while num != guess_num:
    guess_num = int(input("Please enter a number to guess "))
    counter += 1
    if guess_num > num:
        print("The number is greater")
    elif guess_num < num:
        print("The number is lesser")

print(f"You guessed the number {num} right in {counter} tries")