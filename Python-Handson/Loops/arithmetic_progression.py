# Print AP series by taking number and common difference and boundary as input 

a = int(input("Please enter a starting number: "))
d = int(input("Please enter a common difference: "))
b = int(input("Please enter the range boundary: "))

for i in range(a,b,d):
    print(i , end = ',')