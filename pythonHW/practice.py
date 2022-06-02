# Given two integer numbers return product if equal to or lower than 1000
# return sum if greater than 1000

number1 = int(input('What is the first number? '))
number2 = int(input('What is the second number? '))

if (number1 * number2) <= 1000 :
    print(number1 * number2)
else :
    print(number1 + number2)
