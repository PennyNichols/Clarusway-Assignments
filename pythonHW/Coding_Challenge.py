# Find the largest number from a user-input list of any size
# Do not use the max() function

n = int(input("How many numbers will you enter? "))
numbers = []
count = 0

while count < n:
    number = int(input("Pick a number : "))
    numbers.append(number)
    count += 1

largest = numbers[0]  
for i in numbers:
    if i > largest:
        largest = i

print(f'The largest number is: {largest}.')