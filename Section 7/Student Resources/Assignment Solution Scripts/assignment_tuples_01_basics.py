# Tuples
# Assignment 1

tuple_numbers = (1, 2, 3, 4, 5)
tuple_groceries = ('coconuts', 'bananas', 'onions', 'spinach', 'tomatoes', 'cilantro', 'milk')
groceries_inventory = ('coconuts', 'tomatoes', 'onions', 'coconuts', 'bananas', 'onions', 'spinach', 'tomatoes', 'cilantro', 'milk', 'spinach', 'tomatoes', 'cilantro', 'tomatoes')
tuple_nested =((1, 2, 3), ["Python", "Database", "System"], 'Coding')
tuple_numbers_100s = (100, 200, 300, 400, 500)


# Print 3rd item from  tuple_groceries
print("*" * 50)
print("The 3rd item of tuple_groceries :", tuple_groceries[2])

# Print the length of tuple_groceries
print("*" * 50)
print("The length of tuple_groceries :", len(tuple_groceries))

# Print the reverse of tuple_numbers & tuples_names
print("*" * 50)
tuple_groceries_rev = tuple(reversed(tuple_groceries))
print("Reverse of tuple_groceries :", tuple_groceries_rev)

# Print "Python" from "tuple_nested"
print("*" * 50)
print(tuple_nested[1][0])

# Unpack tuple_groceries tuple and print them
print("*" * 50)
print("Unpacking...")
g1, g2, g3, g4, g5, g6, g7, = tuple_groceries
print(g1)
print(g1)
print(g2)
print(g3)
print(g4)
print(g5)
print(g6)
print(g7)

# Swap tuple_numbers and tuple_numbers_100s
print("*" * 50)
print("Swapping...")
tuple_numbers, tuple_numbers_100s = tuple_numbers_100s, tuple_numbers
print("tuple_numbers_100s :", tuple_numbers_100s)
print("tuple_numbers :", tuple_numbers)

# Construct a new tuple "tuples_a" by extracting
# bananas, onions, spinach from tuples_groceries
print("*" * 50)
print("Subset items.... bananas, onions, spinach")
tuples_a = tuple_groceries[1:4]
print("tuples_a :", tuples_a)


# Count the number of times coconuts is listed in groceries_inventory tuple
print("*" * 50)
print("Count the number of times coconuts...")
coconut_count = groceries_inventory.count("coconuts")
print("coconuts :", coconut_count)
