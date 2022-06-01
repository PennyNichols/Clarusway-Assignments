# Find out if a given number is an "Armstrong Number"
# Armstrong Number --> n-digit number that is the sum of the nth power of its digits
# ex: 371 = 3**3 + 7**3 + 1**3
#    9474 = 9**4 + 4**4 + 7**4 + 4**4
#   93084 = 9**5 + 3**5 + 0**5 + 8**5 + 4**5

# Write a program that:
# 1. Takes a positive integer number from the user
# 2. Checks if it is an Armstrong number
# 3. Consider negatives, floats, and other entries and displays warning

x = input("Please enter a positive integer: ").lower()
x_list = list(x)
x_set = set(x)
letters = set('abcdefghijklmnopqrstuvwxyz')
dec = {".", ","}
neg = {"-",}
num = []
numbers = []
numbers_squared = []

while ((x_set & letters) != set()) or ((x_set & dec) != set()) or ((x_set & neg) != set()) :
    print ("Invalid entry. Do not use non-numeric, float, or negative values!")
    break

else :
    a = len(x)
    num = int(x)
    numbers = [int(number) for number in x_list]
    numbers_squared = [i**a for i in numbers]
    

    if num == sum(numbers_squared) :
        print(f"{x} is an Armstrong number.")

    elif num != sum(numbers_squared) :
        print(f"{x} is not an Armstrong number.")

  