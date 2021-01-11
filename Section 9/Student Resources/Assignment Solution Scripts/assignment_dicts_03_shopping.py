# Dictionaries
# Assignment 3

inventory = {"banana": 0.25,
             "watermelon": 5.25,
             "orange": 0.50,
             "peer": 0.40,
             "apple": 0.30,
             "kiwi": 0.75,
             }

# Print the use
print('Welcome to the ABC fruit shop. Please enter the quantity :')
user_quantity_bananas = int(input('Bananas : '))
user_quantity_Watermelons = int(input('Watermelons : '))
user_quantity_oranges = int(input('orange : '))
user_quantity_peers = int(input('peer : '))
user_quantity_apples = int(input('apple : '))
user_quantity_kiwis = int(input('kiwi : '))

# Calculating cost
total_cost_bananas = user_quantity_bananas * inventory.get("banana")
total_cost_Watermelons = user_quantity_Watermelons * inventory.get("watermelon")
total_cost_oranges = user_quantity_oranges * inventory.get("orange")
total_cost_peers = user_quantity_peers * inventory.get("peer")
total_cost_apples = user_quantity_apples * inventory.get("apple")
total_cost_kiwis = user_quantity_kiwis * inventory.get("kiwi")

total_cost = total_cost_kiwis + total_cost_bananas + total_cost_apples + total_cost_oranges + \
             total_cost_peers + total_cost_Watermelons

print()
print("Please pay ", total_cost)
