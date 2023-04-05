def main():
    num_entries = int(input("How many entries do you want to make? "))

    with open("contacts.txt", "w") as f:
        for i in range(num_entries):
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")

            f.write(f"{name},{phone},{email}\n")

    print("Contact information saved to contacts.txt.")


if __name__ == "__main__":
    main()
