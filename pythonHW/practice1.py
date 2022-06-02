# Write a program to iterate through ten numbers
# In each iteration, print the sum of the current and previous number

previous = 0
sum_x = 0

for i in range(1, 11) :
    sum_x = previous + i
    print(f'Current Number: {i}  Previous Number: {previous}  Sum: {sum_x}')
    previous += 1