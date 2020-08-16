print("Let's play rock paper scissors!")
choice1 = input("Enter player 1's choice: ")
choice2 = input("Enter player 2's choice: ")

if choice1 == choice2:
    print("It's a draw!")
elif choice1 == "rock":
    if choice2 == "scissors":
        print("Player 1 wins!")
    elif choice2 == "paper":
        print("Player 2 wins!")
elif choice1 == "paper":
    if choice2 == "rock":
        print("Player 1 wins!")
    elif choice2 == "scissors":
        print("Player 2 wins!")
elif choice1 == "scissors":
    if choice2 == "paper":
        print("Player 1 wins!")
    elif choice2 == "rock":
        print("Player 2 wins!")
elif not choice1 or not choice2:
    print("Please enter a choice")
else:
    print("Something went wrong!")