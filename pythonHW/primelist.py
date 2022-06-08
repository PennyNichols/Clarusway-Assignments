# list all prime numbers beneath a user-input limit

limit = int(input("Please enter an upper limit: "))
prime = []
for number in range(2,(limit+1)):
    if number>1:
        for i in range(2,number):
            if (number%i)==0:
                break
        else:
            prime.append(number)
print(prime)

