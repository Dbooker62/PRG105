monthlyIncome = float(input("How much is your total monthly income? "))
housing= float(input("How much do you spend on housing each month? "))
food= float(input("How much do you spend on food each month? "))
transportation= float(input("How much do you spend on transportation each month? "))
Phone= float(input("How much do you spend on phone bill each month? "))
Utilities=float(input("How much do you spend on utilities bill each month? "))
clothing=float(input("How much do you spend on clothing bill each month? "))

housing_pct = (housing / monthlyIncome) * 100
food_pct = (food /monthlyIncome) * 100
transportation_pct= (transportation/monthlyIncome) *100
phone_pct= (Phone/monthlyIncome) *100
Utilities_pct= (Utilities/monthlyIncome) *100
clothing_pct= (clothing/monthlyIncome) *100

remaining_money= monthlyIncome-(housing+food+transportation+Phone+Utilities+clothing)

#display results
print("Housing takes up {:.2f}% of your monthly income.".format(housing_pct))
print("Food takes up {:.2f}% of your monthly income.".format(food_pct))
print("Transportation takes up {:.2f}% of your monthly income.".format(transportation_pct))
print("Phone takes up {:.2f}% of your monthly income.".format(phone_pct))
print("Utilities takes up {:.2f}% of your monthly income.".format(Utilities_pct))
print("Clothing takes up {:.2f}% of your monthly income.".format(clothing_pct))

print("You have ${:.2f} left from your income after paying these monthly expenses.".format(remaining_money))
