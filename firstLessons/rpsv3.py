import random

player_wins = 0
computer_wins = 0
winning_score = 4
while player_wins < winning_score and computer_wins < winning_score:
    print("Let's play rock paper scissors!")
    print(f"Computer Score: {computer_wins} ... Player Score: {player_wins}")
    choice1 = input("Enter your choice: ").lower()

    cpu = random.randint(0, 2)

    rps = ["rock", "paper", "scissors"]

    com_choice = rps[cpu]

    print("Computer picks: " + com_choice)

    if choice1:
        if choice1 == "quit":
            break
        elif choice1 != rps[0] and choice1 != rps[1] and choice1 != rps[2]:
            print("Please enter a valid choice!")
        elif choice1 == com_choice:
            print("It's a draw!")
        elif choice1 == "rock" and com_choice == "scissors":
                print("You win!")
                player_wins += 1
        elif choice1 == "paper" and com_choice == "rock":
                print("You win!")
                player_wins += 1
        elif choice1 == "scissors" and com_choice == "paper":
                print("You win!")
                player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
    else:
        print("Please enter a choice")
print("Final scores:")
print(f"Computer score: {computer_wins}")
print(f"Player score: {player_wins}")
if player_wins > computer_wins:
    print("Congrats! You won!")
else: 
    print("You lose. Try again later!")