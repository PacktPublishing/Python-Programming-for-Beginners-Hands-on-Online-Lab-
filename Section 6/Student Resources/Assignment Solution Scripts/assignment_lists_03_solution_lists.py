# Lists
# Assignment 4

shopping_list = ['coconuts', 'bananas', 'onions', 'spinach', 'tomatoes', 'cilantro', 'milk']

# print shopping list
print(shopping_list)

# If garlic is not present, add it
if "garlic" not in shopping_list:
    shopping_list.append("garlic")
print(shopping_list)

# Remove onions from the list
onions_index = shopping_list.index("onions")
del shopping_list[onions_index]
print(shopping_list)

# Add chips and bread
shopping_list.append("chips")
shopping_list.append("bread")
print(shopping_list)

# Insert oranges before bananas
spinach_index = shopping_list.index("bananas")
shopping_list.insert(spinach_index, "oranges")
print(shopping_list)


