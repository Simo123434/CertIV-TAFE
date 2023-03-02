import random

print("Welcome to the guessing game \n You can select how big the range is")

userRange = int(input("Enter your range: "))


number = random.randint(1, userRange)
num_guesses = 5

while num_guesses > 0:
    try:
        guess = int(input(f"Guess a number between 1 and {userRange}: "))
    except ValueError:
        print("Enter a number you numpty")
        continue

    if guess == number:
        print(f"Congratulations! You guessed the number in {5-num_guesses} guesses!")
        break
    elif guess < number:
        print("Too low!")
        num_guesses -= 1
    else:
        print("Too high!")
        num_guesses -= 1

    print("You have", num_guesses, "guesses remaining.")
    
if num_guesses == 0:
    print("Sorry, you ran out of guesses. The number was", number)

