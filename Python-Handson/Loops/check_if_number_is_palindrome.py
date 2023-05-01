# Check if a given number is palindrome or not

num = int(input("Please enter a number that you want to compare: "))
orig_num = num
counter = 0
rev_num = 0

while num > 0:
    rem = num % 10
    rev_num = rev_num * 10 + rem
    num = num // 10
    counter += 1
    
if orig_num == rev_num:
    print(f"The number {orig_num} is palindrome")
else:
    print(f"The number {orig_num} is not a palindrome")