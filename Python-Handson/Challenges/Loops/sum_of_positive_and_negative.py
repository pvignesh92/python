# Need to identify the sum of the positive and negative numbers given as input from the user seprately

nums_input = int(input("Please enter the number of numbers that you are going to input: "))
pos_sum = 0
neg_sum = 0 

while nums_input > 0:
    num = int(input("Please enter the number: "))
    print(f"The number entered is {num}")
    if num > 0:
        pos_sum = pos_sum + num
    else:
        neg_sum = neg_sum + num
    nums_input = nums_input - 1

print(f"The sum of the positive numbers is {pos_sum} and negative numbers is {neg_sum}")