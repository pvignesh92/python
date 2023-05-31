# Print Multiplication table for a given number till 10 times 

num = int(input("Please enter a number for multiplication table: "))
counter = 1

while counter <= 10:
    print(f"{counter} * {num} = {counter * num}")
    counter +=  1



