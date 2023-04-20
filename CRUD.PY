import pickle


LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
FILE_NAME = "customer_file.pickle"


def main():
    try:
        with open(FILE_NAME, 'rb') as file:
            customer_file = pickle.load(file)
    except:
        customer_file = {}

    choice = 0
    while choice != QUIT:
        choice = menu()
        if choice == LOOK_UP:
            read(customer_file)
        elif choice == ADD:
            create(customer_file)
        elif choice == CHANGE:
            update(customer_file)
        elif choice == DELETE:
            delete(customer_file)

    save(customer_file)

def menu():
    print("Main Menu")
    print("1. Look up an email address")
    print("2. Add a new name and email address")
    print("3. Change an email address")
    print("4. Delete a name and email address")
    print("5. Quit the program")
    choice = 0
    while choice < 1 or choice > 5:
        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Invalid choice. Please enter a number between 1 and 5.")
    return choice

def read(customer_file):
    customer_name = input("Enter a name: ")
    if customer_name in customer_file:
        print("Email address:", customer_file[customer_name])
    else:
        print("Name not found.")


def create(customer_file):
    customer_name = input("Enter a name: ")
    if customer_name not in customer_file:
        customer_email = input("Enter an email address: ")
        customer_file[customer_name] = customer_email
        print("Data added.")
    else:
        print("Name already exists.")

def update(customer_file):
    customer_name = input("Enter a name: ")
    if customer_name in customer_file:
        print("Email address:", customer_file[customer_name])
        confirm = input("Change email address? (Y/N) ")
        if confirm.upper() == 'Y':
            customer_email = input("Enter new email address: ")
            customer_file[customer_name] = customer_email
            print("Data updated.")
        else:
            print("No changes made.")
    else:
        print("Name not found.")

def delete(customer_file):
    customer_name = input("Enter a name: ")
    if customer_name in customer_file:
        print("Email address:", customer_file[customer_name])
        confirm = input("Delete this entry? (Y/N) ")
        if confirm.upper() == 'Y':
            del customer_file[customer_name]
            print("Data deleted.")
        else:
            print("No changes made.")
    else:
        print("Name not found.")

def save(customer_file):
    try:
        with open(FILE_NAME, 'wb') as file:
            pickle.dump(customer_file, file)
    except:
        print("Unable to save file.")

main()
