# Lists
# Assignment 1

numbers = [10, 8, 4, 5, 6, 9, 2, 3, 0, 7, 2, 6, 6]
animals = ['lion', 'tiger', 'dog', 'cat', 'goat', 'donkey', 'horse', 'hen', 'fox', 'elephant', 'snake', 'pig']

# Get the 4th item from animals
print("The 4th item in animals : ", animals[3])

# Get the last item from animals
print()
print("The last item in animals : ", animals[-1])

# Get 3rd to 10th items from animals
print()
print('3rd to 10th items : ', animals[2:10])

# Determine the total number of items in animals
print()
print('Length of animals : ', len(animals))

# Determine the sum of all items & product of all items in numbers
print()
print("Sum of all items & product of all items in numbers:")
all_items_total = 0
all_items_product = 1


for num in numbers:
    all_items_total += num
    if num != 0:
        all_items_product *= num

print("numbers :", numbers)
print("Sum of all items : ", all_items_total)
print("Product of all items : ", all_items_product)