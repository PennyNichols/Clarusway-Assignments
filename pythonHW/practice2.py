# Write a program that recieves a word input from user
# iterates through the string
# prints all even numbered indexes

word = input('Please enter a word: ')
length = len(word)

for i in range(0,length,2) :
    print(word[i])