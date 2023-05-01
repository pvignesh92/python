# Find the factorial of a given number

n = int(input("Please enter the number you want to run factorial: "))
fact = 1

for i in range(1,n+1):
    fact = fact * i
print(f"The factorial of {n} is {fact}")