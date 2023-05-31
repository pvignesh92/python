# Sum of digits in a number

num = int(input("Please enter a number that you want to sum the digits: "))
orig_num = num
counter = 0
rem = 0
sum = 0 

while num > 0:
    rem = num % 10
    sum = rem + sum
    num = num // 10
    counter += 1
    

print(f"The Sum of digits in {orig_num} is {sum}")