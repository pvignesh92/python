# Count the number of digits in a number

num = int(input("Please enter a number that you want to count digits for: "))
orig_num = num
counter = 0

while num > 0:
    num = num // 10
    counter += 1
    

print(f"The total number of digits in {orig_num} is {counter}")