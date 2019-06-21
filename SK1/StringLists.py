"""Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)"""

strValue = input("Please enter a string to check, whether it is palindrome or not:")
if strValue[::-1] == strValue:
    print("It is palindrome")
else:
    print("It is not palindrome")
