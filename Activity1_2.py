
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
max = num1

if num2 > max:
    max = num2
if num3 > max:
    max = num3

print("The maximum number among the 3 numbers is: ", max)