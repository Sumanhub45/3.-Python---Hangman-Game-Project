Hangman Game


This is a simple Python Hangman game with a graphical user interface (GUI) built using the Tkinter library. In this game, you try to guess a hidden word by suggesting letters one at a time. You have a limited number of attempts to guess the word correctly.


Getting Started
These instructions will help you run the Hangman game on your local machine.

Prerequisites
You need to have Python installed on your system to run this program. Tkinter is included with most Python installations, so you don't need to install it separately.

Running the Game
Clone this repository to your local machine or download the script.

Open your terminal or command prompt.

Navigate to the directory where the 3.HangmanGame.py file is located.

Run the following command to start the Hangman game:


python 3.HangmanGame.py
The Hangman game GUI will open, and you can start playing.

How to Play
The game will choose a random word from the predefined list.

You will see a series of underscores representing the hidden word. Each underscore represents a letter in the word.

Enter a single letter in the input field and click the "Guess" button to make a guess.

If your guess is correct and the letter is in the word, it will be revealed in its correct position(s).

If your guess is incorrect, you will lose one attempt.

You have a limited number of attempts (default: 6) to guess the word correctly.

Continue guessing letters until you either guess the word correctly or run out of attempts.

If you guess the word correctly, you win the game.

If you run out of attempts, the game is over, and the word is revealed.

Customization
You can customize the game by modifying the list of words in the words variable at the beginning of the script. You can also adjust the number of attempts by changing the self.attempts value in the HangmanGame class constructor.