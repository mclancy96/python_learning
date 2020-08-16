import random

rand = random.randint(1,10)
print("I have generated a random number between 1 and 10 for you to guess.")
guess = None

while True:
    guess = input("Enter your guess here: ")
    if guess == "exit":
        print("You have chosen the coward's way out. Bye, loser")
        break
    else:
        guess = int(guess) 
    if guess > rand:
        print("That number is too high. Guess again or type \"exit\" to end the program.")
    elif guess < rand:
        print("That number is too low. Guess again or type \"exit\" to end the program.")
    elif guess == rand:
        print("Correct! You win! Would you like to play again? (y/n)")
        res = input()
        if res == "n":
            print("Goodbye!")
            break
        else:
            rand = random.randint(1,10)
            print("I have generated a new random number between 1 and 10 for you to guess.")
            guess = None
    else:
        break



