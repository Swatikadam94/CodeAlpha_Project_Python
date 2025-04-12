import random

def hangman():
    # List of words for the game
    words = ["python", "hangman", "programming", "developer", "computer"]
    word = random.choice(words).lower()
    guessed_word = ["_" for _ in word]
    guessed_letters = set()
    attempts = 6  # Number of incorrect guesses allowed

    print("Welcome to Hangman!")
    print("Guess the word:", " ".join(guessed_word))

    while attempts > 0 and "_" in guessed_word:
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts remaining.")

        print("Word:", " ".join(guessed_word))

    if "_" not in guessed_word:
        print("\nCongratulations! You've guessed the word:", word)
    else:
        print("\nGame Over! The word was:", word)

# Run the game
hangman()



