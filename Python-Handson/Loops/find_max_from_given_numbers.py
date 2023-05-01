# Find the maximum of numbers given as input from the user
nums_input = int(input("Please enter the number of numbers that you are going to input: "))
max_num = 0

while nums_input > 0:
    num = int(input("Please enter the number: "))
    print(f"The number entered is {num}")
    if num > max_num:
        max_num = num
    nums_input = nums_input - 1

print(f"The max number is {max_num}")