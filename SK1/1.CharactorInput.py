"""Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:
Add on to the previous program by asking the user for another number and printing out that many copies
of the previous message.(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button)
"""
name = input("Please enter your name :")
age = int(input("Please enter your age :"))
print("Hi {0},\n\nYou will become 100 year on {1}".format(name, 2019-age+100))
print("Thanks")