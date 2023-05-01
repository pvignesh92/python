# Print n terms of Fibanocci series 

n = int(input("Please enter the number: "))

a = 0
b = 1

for i in range(n):
    print(a, end = ",")
    c = a + b 
    a = b
    b = c