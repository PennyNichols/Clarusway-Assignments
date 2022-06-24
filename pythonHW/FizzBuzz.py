# Print the Fizz Buzz numbers

# print numbers 1-100, inclusive
# multiples of 3 should print 'Fizz'
# multiples of 5 should print 'Buzz'
# multiples of 3 and 5 should print 'FizzBuzz'
# all other numbers should print the number
# each output value should be a separate line

def fizzbuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()
