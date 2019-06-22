"""Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
 compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock"""

player1 = input("Please enter the name for player1:")
player2 = input("Please enter the name for player2:")

p1_value =input("Please enter your choise for {0}:".format(player1))
p2_value =input("Please enter your choise for {0}:".format(player2))

print(player1 + " " + p1_value)
print(player2 + " " + p2_value)