# Sum of digits in a number

num = int(input("Please enter a number that you want to reverse: "))
orig_num = num
counter = 0
rev_num = 0

while num > 0:
    rem = num % 10
    rev_num = rev_num * 10 + rem
    num = num // 10
    counter += 1
    
print(f"The reverse of {orig_num} is {rev_num}")