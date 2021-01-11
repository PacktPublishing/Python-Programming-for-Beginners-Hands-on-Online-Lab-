# Dictionaries
# Assignment 2
# Find the aisle number based on the item

aisles = {"A100": ['bananas', 'milk', 'bread'],
          "A101": ['pens', 'pencils', 'paper'],
          "A102": ['canned peas', 'canned carrots', 'canned beans'],
          "A103": ['plates', 'glasses', 'table cloth']
          }

# Prompt user
user_input = input('What are you looking for : ')

# Get the Aisle
print()
for aisle in aisles.keys():
    aisle_list = aisles[aisle]
    if user_input in aisle_list:
        print(user_input, "is on aisle", aisle)

# Add new aisle B101 with Kids_toys, Kids_cloths
aisles["B101"] = ['kids toys', 'kids clothes']

# Printing using for loop
print()
for aisle in aisles:
    print(aisle, ":", aisles[aisle])
