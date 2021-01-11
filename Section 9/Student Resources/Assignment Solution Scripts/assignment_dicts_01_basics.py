# Dictionaries
# Assignment 1


aisles = {"A100": ['bananas', 'milk', 'bread'],
          "A101": ['pens', 'pencils', 'paper'],
          "A102": ['canned_peas', 'canned_carrots', 'canned_beans'],
          "A103": ['plates', 'glasses', 'table_cloth']
          }

dict_employee_IDs = {"ID01": 'John Papa',
                     "ID02": 'David Thompson',
                     "ID03": 'Terry Gao',
                     "ID04": 'Barry Tex'}

# Who is ID02
name = dict_employee_IDs.get("ID02")
print("ID02 is", name)

# Delete aisle A102
print()
del aisles["A102"]
print(aisles)


