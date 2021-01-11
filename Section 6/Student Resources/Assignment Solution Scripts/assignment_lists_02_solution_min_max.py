# Lists
# Assignment 2

numbers = [10, 8, 4, 5, 6, 9, 2, 3, 0, 7, 2, 6, 6]

min_item = numbers[0]
max_item = numbers[0]

for num in numbers:
    if min_item > num:
        min_item = num

    if max_item < num:
        max_item = num

print("Minimum Number : ", min_item)
print("Maximum Number : ", max_item)