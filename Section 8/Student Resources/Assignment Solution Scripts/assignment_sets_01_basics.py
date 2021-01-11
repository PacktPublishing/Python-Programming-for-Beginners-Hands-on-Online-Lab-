# Sets
# Assignment 1

shop_groceries = {'coconuts', 'bananas', 'onions', 'spinach', 'tomatoes', 'cilantro', 'milk'}
more_groceries = {'bread', 'chips', 'water bottles', 'lemon'}

# Print shop_groceries
print("shop_groceries : ", shop_groceries)

# Add "onions" to shop_groceries
shop_groceries.add("potatoes")
print("shop_groceries : ", shop_groceries)

# Remove "coconuts" from shop_groceries
shop_groceries.discard("coconuts")
print("shop_groceries : ", shop_groceries)

# Adding more_groceries to shop_groceries
print()
print("Updating shop_groceries :")
shop_groceries.update(more_groceries)
print("shop_groceries : ", shop_groceries)
