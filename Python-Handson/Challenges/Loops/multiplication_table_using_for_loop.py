# Display the multiplication table of a given number using For loop 

num = int(input("Please enter the number for multiplication table: "))

for i in range(1,11):
    print(f"{i} * {num} = {i*num}")