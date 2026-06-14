import random


# Predefined list of 5 words

words = ["python", "coding", "program", "mystery", "jupiter"]

secret_word = random.choice(words)


guessed = []

wrong_attempts = 0


print("--- WELCOME TO HANGMAN GAME ---")

print(f"Word length is: {len(secret_word)} letters")


while wrong_attempts < 10:

    # Build the display string to show progress

    display = ""

    for letter in secret_word:

        if letter in guessed:

            display += letter + " "

        else:

            display += "_ "

            

    print("\nWord:", display.strip())

    print(f"Wrong attempts left: {10 - wrong_attempts}")

    print(f"Letters tried: {guessed}")


    # Win condition check

    if "_" not in display:

        print("\nNice! You won the game! 🎉")

        break


    # Get user input

    guess = input("Guess a letter: ").lower()


    # Basic input validation

    if len(guess) != 1 or not guess.isalpha():

        print("Please enter a single valid letter.")

        continue

        

    if guess in guessed:

        print("You already tried that letter!")

        continue


    # Add the guess to the tracker list

    guessed.append(guess)


    # Check if the guess is right or wrong

    if guess in secret_word:

        print("Correct!")

    else:

        print("Wrong guess!")

        wrong_attempts += 1


# Lose condition check

if wrong_attempts == 10:

    print("\nGame Over! You lost.")

    print(f"The word was: {secret_word}")

