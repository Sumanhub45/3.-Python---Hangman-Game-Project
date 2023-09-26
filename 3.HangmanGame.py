
import tkinter as tk
import random

# List of words for the game
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(words)

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        
        self.word_to_guess = choose_word()
        self.guessed_letters = []
        self.attempts = 6  # You can adjust the number of attempts
        
        self.word_label = tk.Label(master, text=self.display_word())
        self.word_label.pack(pady=10)
        
        self.attempts_label = tk.Label(master, text=f"Attempts left: {self.attempts}")
        self.attempts_label.pack()
        
        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack(pady=10)
        
        self.guess_button = tk.Button(master, text="Guess", command=self.make_guess)
        self.guess_button.pack()
        
        self.message_label = tk.Label(master, text="")
        self.message_label.pack(pady=10)
        
    def display_word(self):
        display = ""
        for letter in self.word_to_guess:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += "_"
        return display
    
    def make_guess(self):
        guess = self.guess_entry.get().lower()
        
        if len(guess) != 1 or not guess.isalpha():
            self.message_label.config(text="Please enter a single letter.")
        elif guess in self.guessed_letters:
            self.message_label.config(text="You already guessed that letter.")
        else:
            self.guessed_letters.append(guess)
            if guess in self.word_to_guess:
                self.message_label.config(text="Good guess!")
            else:
                self.message_label.config(text="Incorrect guess.")
                self.attempts -= 1
            
            self.attempts_label.config(text=f"Attempts left: {self.attempts}")
            self.word_label.config(text=self.display_word())
            
            if set(self.guessed_letters) == set(self.word_to_guess):
                self.message_label.config(text=f"Congratulations! You guessed the word: {self.word_to_guess}")
                self.guess_entry.config(state="disabled")
            elif self.attempts == 0:
                self.message_label.config(text=f"Sorry, you ran out of attempts. The word was: {self.word_to_guess}")
                self.guess_entry.config(state="disabled")

# Create the main window
root = tk.Tk()

# Start the game
game = HangmanGame(root)

# Run the GUI
root.mainloop()
