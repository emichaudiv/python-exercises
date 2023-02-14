import random

# Set our game ending flag to False
game_running = True

while game_running:
    # Greet the user to our game
    print()
    print("I'm thinking of a number between 1 and 10, can you guess it?")

    # Have the program pick a random number between 1 and 10
    secret_number = random.randint(0, 10)

    # Set the player's guess number to something outside the range
    guess_number = -1

    # Loop until the player guesses our number
    while guess_number != secret_number:

        # Get the player's guess from the player
        print()
        guess = input("Please enter a number: ")

        # Does the user want to quit playing?
        if guess == "quit":
            game_running = False
            break

        # Otherwise, nope, player wants to keep going
        else:
            # Convert the players guess from a string to an integer
            guess_number = int(guess)


        # Did the player guess the program's number?
        if guess_number == secret_number:
            print()
            print("Congratulations, you guessed my number!")

        # Otherwise, whoops, nope, go around again
        else:
            print()
            print("Oh, to bad, that's not my number...")

# Say goodbye to the player
print()
print("Thanks for playing!")