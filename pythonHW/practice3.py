# Iterate through a given list
# Print all items that are divisible by 5

list = [10, 20, 33, 46, 55]
print(f'Given list: {list}')
print('Divisible by 5:')

for i in list :
    if i % 5 == 0 :
        print(i)