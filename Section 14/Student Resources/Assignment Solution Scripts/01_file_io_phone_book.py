# File IO - Append

# File
my_file = "my_phone_book.txt"


# Add
def add_entry(first_name, last_name, phone_number):
    entry = first_name + "," + last_name + "," + phone_number + "\n"
    with open(my_file, "a") as file_handler:
        file_handler.write(entry)


# Get list
def get_list_from_file(file_name):
    phone_book_list = []
    with open(file_name, "r") as file_handler:
        for line in file_handler:
            phone_book_list.append(line.replace("\n", ""))
    return phone_book_list


# Write list to phone book file
def write_list_to_file(phone_book_list, file_name):
    phone_book_string = ""
    for entry in phone_book_list:
        phone_book_string += entry + "\n"

    with open(file_name, "w") as file_handler:
        file_handler.write(phone_book_string)


# Remove
def remove_entry(first_name, last_name):
    phone_book_list = []
    entry = first_name + "," + last_name
    with open(my_file, "r") as file_handler:
        for line in file_handler:
            if entry not in line:
                phone_book_list.append(line.replace("\n", ""))

    write_list_to_file(phone_book_list, my_file)


# Look up
def look_up_name(first_name, last_name):
    entry = first_name + "," + last_name
    with open(my_file, "r") as file_handler:
        for line in file_handler:
            if entry in line:
                print("*" * 30)
                print("Found : ", line.replace("\n", ""))
                print("*" * 30)
            else:
                print("*" * 30)
                print("Not Found")
                print("*" * 30)


# Update
def update_name():
    with open(my_file, "r") as file_handler:
        for line in file_handler:
            print(line, end="")


# Update
def update_phone_number(first_name, last_name, new_phone_number):
    phone_list = get_list_from_file(my_file)
    entry_to_search = first_name + "," + last_name
    remove_entry(first_name, last_name)
    add_entry(first_name, last_name, new_phone_number)


# Main
def main():
    while True:
        print("-" * 30)
        print("Welcome To Phone_Book v1.0")
        print("-" * 30)
        print("Menu :")
        print("1. Add")
        print("2. Lookup")
        print("3. Update Phone Number")
        print("4. Delete")
        print("5. Exit")
        print()
        choice = int(input("Enter your selection : "))

        if choice == 1:
            first_name = input("Enter First Name : ")
            last_name = input("Enter Last Name : ")
            phone_number = input("Enter Phone Number : ")
            add_entry(first_name, last_name, phone_number)

        if choice == 2:
            first_name = input("Enter First Name : ")
            last_name = input("Enter Last Name : ")
            look_up_name(first_name, last_name)

        if choice == 3:
            first_name = input("Enter First Name : ")
            last_name = input("Enter Last Name : ")
            new_phone_number = input("Enter New Phone Number : ")
            update_phone_number(first_name, last_name, new_phone_number)

        if choice == 4:
            first_name = input("Enter First Name : ")
            last_name = input("Enter Last Name : ")
            phone_number = input("Enter Phone Number : ")
            remove_entry(first_name, last_name)

        if choice == 5:
            exit()


if __name__ == "__main__":
    main()
