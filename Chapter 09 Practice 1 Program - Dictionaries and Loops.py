steps_dict = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}

for day in steps_dict.keys():

    while True:
        try:
            steps = int(input(f"Enter the number of steps for {day}: "))
            if steps < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    steps_dict[day] = steps

total_steps = sum(steps_dict.values())

max_steps = max(steps_dict, key=steps_dict.get)

min_steps = min(steps_dict, key=steps_dict.get)

print(f"Total steps: {total_steps}")
print(
    f"Day(s) with the most steps: {', '.join([day for day, steps in steps_dict.items() if steps == steps_dict[max_steps]])}")
print(
    f"Day(s) with the least steps: {', '.join([day for day, steps in steps_dict.items() if steps == steps_dict[min_steps]])}")
