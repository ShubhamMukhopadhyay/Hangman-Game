🎯 Hangman Game in Python

A classic word-guessing game implemented in Python. Players try to guess the hidden word by inputting letters before the hangman figure is fully drawn. This project combines ASCII art, interactive gameplay, colorful terminal output, and Python fundamentals for a fun coding experience.

📝 Table of Contents

About

1. Features
2. Gameplay
3. Installation
4. Usage
5. Folder
6. Structure
7. Contributing
8. License

📌 About

Hangman is a popular guessing game where players reveal a hidden word by guessing letters one at a time. This Python version adds a modern, interactive twist with:

1. Dynamic word list
2. ASCII-art hangman stages
3. Input validation
4. Colorful terminal output
5. Lives tracking and win/loss notifications

It’s perfect for beginners to practice Python loops, conditionals, and modular programming.

✨ Features

1. Random word selection from a large list
2. Graphical representation of the hangman using ASCII art
3. Clear display of guessed letters and remaining blanks
4. Input validation: prevents repeated guesses and invalid entries
5. Live tracking of lives remaining
6. Win/Loss messages with color and emojis for enhanced UX
7. Easy-to-read code structure and modular design for learning

🎮 Gameplay

1. Run the game in your terminal or IDE.
2. A random word is selected from the list.
3. Players input one letter at a time.
4. Correct guesses reveal the letter in the word.
5. Incorrect guesses reduce lives and reveal the hangman stage.
6. Game ends when the word is guessed or all lives are lost.

Example ASCII Stage:
   --------
   |      |
   |      O
   |     /|\
   |     / \
   |     
--------

🗂 Folder Structure
hangman/
│
├── main.py            # Main game script
├── hangman_word.py    # Word list
├── hangman_art.py     # ASCII art and logo
└── README.md          # Project documentation

🖥️ How to run
1. Download the zip file
2. and run it
