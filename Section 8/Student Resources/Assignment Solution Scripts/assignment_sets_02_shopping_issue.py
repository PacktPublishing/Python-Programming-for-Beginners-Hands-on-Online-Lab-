# Sets
# Assignment 2

team_a_groceries = {'coconuts', 'bananas', 'onions', 'grapes', 'spinach', 'tomatoes', 'cilantro', 'milk', 'cilantro'}
team_b_groceries = {'peach', 'tomatoes', 'onions', 'grapes', 'bananas', 'onions', 'spinach', 'tomatoes',
                    'cilantro', 'kiwi', 'spinach', 'tomatoes', 'cilantro', 'tomatoes', 'papaya'}

# Print team a groceries
print()
print("team a:")
print(team_a_groceries)

# Print team b groceries
print()
print("team b:")
print(team_b_groceries)

# Print items that are common on both the lists
print()
print("Common:")
print(team_a_groceries.intersection(team_b_groceries))

# Print items that are only on team a's list
print()
print("Only on team a's list:")
print(team_a_groceries.difference(team_b_groceries))

# Print items that are only on team b's list
print()
print("Only on team b's list:")
print(team_b_groceries.difference(team_a_groceries))

# Print a master list that includes items from both the lists
print()
print("Consolidated list:")
print(team_a_groceries.union(team_b_groceries))

print()
print("Consolidated list of items that are present only on one list:")
print(team_a_groceries.symmetric_difference(team_b_groceries))
