customer_info = []
try:
    with open("accounts.txt", "r") as accounts_file:
        for line in accounts_file:
            customer_info.append(line.strip())
except FileNotFoundError:
    print("Error: File 'accounts.txt' not found")
    exit(1)
except Exception as e:
    print(f"Error: Failed to read 'accounts.txt' - {e}")
    exit(1)

overdue_accounts = []
try:
    with open("over90.txt", "r") as over90_file:
        for line in over90_file:
            overdue_accounts.append(line.strip())
except FileNotFoundError:
    print("Error: File 'over90.txt' not found")
    exit(1)
except Exception as e:
    print(f"Error: Failed to read 'over90.txt' - {e}")
    exit(1)

for customer in customer_info:
    customer_data = customer.split(",")
    customer_number = customer_data[0].strip()
    if customer_number in overdue_accounts:

        print(f"Customer Information: {customer}")
    else:

        print(f"Customer {customer_number} is not overdue")
