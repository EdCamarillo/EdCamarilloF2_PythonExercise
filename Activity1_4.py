
n = int(input("Enter n: "))

count = 0
total = 0

for count in range(n + 1):
    total += count

print("Sum of all numbers from 1 to", n, ": ", total)