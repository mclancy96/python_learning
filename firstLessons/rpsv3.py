import random

print("Let's play rock paper scissors!")
choice1 = input("Enter your choice: ").lower()

cpu = random.randint(0, 2)

rps = ["rock", "paper", "scissors"]

com_choice = rps[cpu]

print("Computer picks: " + com_choice)

if choice1:
    if choice1 != rps[0] and choice1 != rps[1] and choice1 != rps[2]:
        print("Please enter a valid choice!")
    elif choice1 == com_choice:
        print("It's a draw!")
    elif choice1 == "rock" and com_choice == "scissors":
            print("You win!")
    elif choice1 == "paper" and com_choice == "rock":
            print("You win!")
    elif choice1 == "scissors" and com_choice == "paper":
            print("You win!")
    else:
        print("Computer wins!")
else:
    print("Please enter a choice")