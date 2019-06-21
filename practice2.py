"""
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""
value = int(input("Please enter any number to check:"))

isEven = True if value%2 == 0 else False

if isEven:
    print("The number({0}) is {1}".format(value,"even"))
else:
    print("The number({0}) is {1}".format(value, "odd"))
