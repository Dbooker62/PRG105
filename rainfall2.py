data = []
with open("rainfall-totals.txt", "r") as file:
    for line in file:
        data.append(line.strip())

total_rainfall = 0.0
valid_data_count = 0

for entry in data:

    month, rainfall = entry.split()

    if month in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                 "November", "December"]:
        try:
            rainfall = float(rainfall)

            total_rainfall += rainfall
            valid_data_count += 1
        except ValueError:

            print(f"Error: Invalid rainfall value '{rainfall}' for month '{month}'")
    else:

        print(f"Error: Invalid month '{month}'")

average_rainfall = total_rainfall / valid_data_count if valid_data_count > 0 else 0

print(f"Total rainfall: {total_rainfall:.2f} inches")
print(f"Average rainfall: {average_rainfall:.2f}inches")
