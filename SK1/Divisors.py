"""Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
 (If you don’t know what a divisor is, it is a number that divides evenly into another number.
 For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

inputNum = int(input("Enter the number:"))
divisor = []
for num in range(2, inputNum):
    if inputNum % num == 0:
        divisor.append(num)
print("Divisor for {0} are {1}".format(inputNum, divisor))
