"""Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
 compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock"""

player1 = input("Please enter the name for player1:")
player2 = input("Please enter the name for player2:")


def compare(p1,p2):
    value = ["rock","scissor","paper"]
    if p1 in value and p2 in value:
        if p1 == p2:
            print("It is tie.")
        if p1 == "rock":
            if p2 == "scissor":
                print("{0} wins".format(player1))
            else:
                print("{0} wins".format(player2))
        elif p1 == "scissor":
            if p2 == "paper":
                print("{0} wins".format(player1))
            else:
                print("{0} wins".format(player2))
        else:
            if p2 == "scissor":
                print("{0} wins".format(player1))
            else:
                print("{0} wins".format(player2))
    else:
        print("Values not correct")



while True:
    p1_value = input("Please enter your choise for {0}:".format(player1))
    p2_value = input("Please enter your choise for {0}:".format(player2))
    compare(str.lower(p1_value),str.lower(p2_value))

    conf =input("Do you want to play more:")
    if  str.lower(conf) == 'no':
        break
    else:
        print(str(conf).encode())

#hkjhk
