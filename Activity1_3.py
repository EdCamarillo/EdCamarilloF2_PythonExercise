
num = int(input("Please enter a number: "))

num_digits = 0
smallest = 9
highest = 0

while num != 0:
    digit = num % 10
    num = num // 10

    num_digits = num_digits + 1

    if digit < smallest:
        smallest = digit
    if digit > highest:
        highest = digit

print("Number of digits in the given number is: ", num_digits)
print("Smallest number is: ", smallest)
print("Highest number is: ", highest)

