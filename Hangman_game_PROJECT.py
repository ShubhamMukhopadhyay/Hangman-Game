import random

# Update the word list to use 'word_list' from hangman_words.py
from hangman_word import word_list

from hangman_art import stages

from hangman_art import logo

# Create a variable called lives to keep track of the number of lives left
lives = 6

# Randomly choose a word form the word_list and assign it to a variable called chosen_word. Then print it
chosen_word = random.choice(word_list)

# Create a "placeholder" with the same no. of blanks as the chosen_word
placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"

print(placeholder)

# Use a while loop to let the user guess again
game_over = False

correct_letters = []

print("\033[96m" + logo + "\033[0m")  # Cyan color
print("\nWelcome to \033[93mHangman!\033[0m 🎯")
print("Guess the word before the man hangs! 🪓\n")

while not game_over:

    # Update the code below to tell the user how many lives they have left
    print(f"***********************{lives}/6 LIVES LEFT ***********************")

    #  Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase
    guess = input("Guess a letter: ").lower()


    # If the user has entered a letter they've already guessed, print the letter and let them know
    if guess in correct_letters:
        print(f"You have already guess {guess}")

    # Create a "Display" that puts the guess letter in the right position and _in the same position as the letter
    display = ""

    # To Check if the letter the user guesses(guess) is one of the letters in the chosen_word. Print "Right" if it is, "wrong" if it's not.
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)  # Change the for loop so that you keep the previous correct letters in display

        elif letter in correct_letters:
            display += letter

        else:
            display += "_"

    print("words to guess: " + display)

    # If guess is not a letter in the chosen_word, then reduce lives by1
    # If lives goes down to 0, then the game should end, and it should print "You loose"

    # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You loose a life.")

        if lives == 0:
            game_over = True

            # Update the print statement below to give the user the correct word
            print(f"************************IT WAS {chosen_word}! You loose! ************************")

    if "_" not in display:
        game_over = True
        print("*************************** You win. *************************** ")

    # Print the ASCII art from the "stages" that corresponds to the current number of 'lives' the user has remaining

    print(stages[lives])
