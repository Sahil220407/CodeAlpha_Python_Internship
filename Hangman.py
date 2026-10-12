
import random

# List of 5 predefined words
words = ["python", "computer", "coding", "program", "developer"]

# Select a random word
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("===== WELCOME TO HANGMAN GAME =====")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses allowed.\n")

while wrong_guesses < max_wrong_guesses:
    # Display the word with hidden letters
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)

    # Check whether the word is completely guessed
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!\n")
    else:
        wrong_guesses += 1
        print("Wrong guess!\n")

else:
    print("Game Over! You ran out of guesses.")
    print("The correct word was:", word)
