total_sales = 0
num_sales = 0
good_sales = 0

file_name = input("Please enter the name of the data file: ")

try:
    with open(file_name) as sales_file:
        for line in sales_file:
            try:
                sales = float(line)
            except ValueError:
                print("Bad data:", line)
                continue

            num_sales += 1

            if sales >= 0:
                total_sales += sales
                good_sales += 1

except IOError:
    print("Error: Could not open file", file_name)
    exit()

if num_sales == 0:
    print("No valid sales data found.")
else:
    average_sales = total_sales / good_sales
    print("Total sales:", total_sales)
    print("Average sales:",average_sales)
