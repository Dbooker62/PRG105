def read_sales(filename):
    total = 0.0
    count = 0

    with open(filename, "r") as f:
        for line in f:
            value = float(line.strip())

            total += value

            count += 1

            print("{:.2f}".format(value))

    average = total / count if count > 0 else 0.0

    print("Total: {:.2f}".format(total))
    print("Count: {}".format(count))
    print("Average: {:.2f}".format(average))


if __name__ == "__main__":
    filename = "sales_totals.txt"
    read_sales(filename)
