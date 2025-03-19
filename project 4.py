import random
def main():
    while True: 
        play = (input("Would you like to play a game? "))
        if play == "no":
            print("goodbye")
            break
        else:
            strikes = 6
            targetnum = random.randint(1,100)
            guess = 0 
            while (strikes > 0 and guess != targetnum):
                guess = int(input("Guess a number between 1 and 100: "))
                if (guess > 100 and guess < 1):
                    strikes = strikes - 1
                    print(f"You have {strikes} strikes left")
                else:
                    if (guess > targetnum):
                        strikes = strikes - 1
                        print(f"Sorry, {guess} is too high")
                        print(f"You have {strikes} strikes left")
                    elif (guess < targetnum):
                        strikes = strikes - 1
                        print(f"Sorry, {guess} is too low")
                        print(f"You have {strikes} strikes left")
            if guess == targetnum:
                print("Correct!")
            else:
                print(f"you are out of strikes. The secret number was {targetnum} You lose.")
        play_again = input("Do you want to play again? (yes or no) ")
        if play_again == "no":
            print("Goodbye!")

main()