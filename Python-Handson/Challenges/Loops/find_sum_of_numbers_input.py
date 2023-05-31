# Need to identify the sum of the numbers given as input from the user

nums_input = int(input("Please enter the number of numbers that you are going to input: "))
sum = 0 
while nums_input > 0:
    num = int(input("Please enter the number: "))
    print(f"The number entered is {num}")
    sum = sum + num
    nums_input = nums_input - 1

print(f"The sum of the numbers is {sum}")