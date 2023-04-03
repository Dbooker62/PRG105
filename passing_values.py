def main():

    num = int(input("Enter a whole number between 20 and 100: "))

    good_number = validate(num)


    divisible_by_2 = is_divisible_by_2(good_number)
    divisible_by_3 = is_divisible_by_3(good_number)
    divisible_by_5 = is_divisible_by_5(good_number)


    display_results(good_number, divisible_by_2, divisible_by_3, divisible_by_5)

def validate(num):

    while num < 20 or num > 100:
        num = int(input("Enter a valid whole number between 20 and 100: "))
    return num

def is_divisible_by_2(num):
    return num % 2 == 0

def is_divisible_by_3(num):
    return num % 3 == 0

def is_divisible_by_5(num):
    return num % 5 == 0

def display_results(num, divisible_by_2, divisible_by_3, divisible_by_5):
    print(f"Number: {num}")
    print(f"Divisible by 2: {divisible_by_2}")
    print(f"Divisible by 3: {divisible_by_3}")
    print(f"Divisible by 5: {divisible_by_5}")


main()
