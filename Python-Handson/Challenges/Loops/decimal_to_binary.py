# Convert the number to binary 
num = int(input("Enter the number you want to convert to binary: "))
# Ex for 11 it will be 1011
orig_num = num
bin = 0
rem = 0

while num > 0:
    rem = num%2
    num = num // 2
    bin = bin * 10 + rem

# This will give us the decimal conversion values and we need to reverse to get the actual values
rev_bin = 0

while bin > 0:
    rem = bin%10
    rev_bin = rev_bin * 10 + rem 
    bin = bin // 10
    
print(f"The binary conversion of {orig_num} is {rev_bin}")