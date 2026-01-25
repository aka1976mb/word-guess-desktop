import tkinter as tk
import random
from pathlib import Path

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Word Guess")
        self.geometry("400x300")

        self.word_list = self.load_words()
        self.secret_word = ""
        self.guesses_left = 6
        self.guessed_letters = set()
        self.current_display = ""

        self.word_label = tk.Label(self, text="", font=("Arial", 24))
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(self, width=3, font=("Arial", 18))
        self.entry.pack()
        self.entry.bind("<Return>", self.process_guess)

        self.guess_button = tk.Button(self, text="Guess", command=self.process_guess)
        self.guess_button.pack(pady=10)

        self.guesses_left_label = tk.Label(self, text="", font=("Arial", 12))
        self.guesses_left_label.pack()

        self.guessed_letters_label = tk.Label(self, text="", font=("Arial", 12))
        self.guessed_letters_label.pack()
        
        self.message_label = tk.Label(self, text="", font=("Arial", 12))
        self.message_label.pack()

        self.new_game()

    def load_words(self):
        try:
            words_path = Path(__file__).parent.parent / "words" / "en.txt"
            with open(words_path, "r", encoding="utf-8") as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            return ["default"]

    def new_game(self):
        self.secret_word = random.choice(self.word_list).lower()
        self.guesses_left = 6
        self.guessed_letters = set()
        self.update_display()
        self.message_label.config(text="")
        self.entry.delete(0, tk.END)


    def update_display(self):
        self.current_display = " ".join([char if char in self.guessed_letters else "_" for char in self.secret_word])
        self.word_label.config(text=self.current_display)
        self.guesses_left_label.config(text=f"Guesses left: {self.guesses_left}")
        self.guessed_letters_label.config(text=f"Guessed letters: {', '.join(sorted(self.guessed_letters))}")
        
    def process_guess(self, event=None):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if not guess.isalpha() or len(guess) != 1:
            self.message_label.config(text="Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            self.message_label.config(text="You already guessed that letter.")
            return

        self.guessed_letters.add(guess)

        if guess not in self.secret_word:
            self.guesses_left -= 1
            self.message_label.config(text=f"Wrong guess!")
        else:
            self.message_label.config(text="Correct guess!")

        self.update_display()
        self.check_game_over()

    def check_game_over(self):
        if all(char in self.guessed_letters for char in self.secret_word):
            self.message_label.config(text=f"You won! The word was '{self.secret_word}'.")
            self.prompt_new_game()
        elif self.guesses_left <= 0:
            self.message_label.config(text=f"You lost! The word was '{self.secret_word}'.")
            self.word_label.config(text=" ".join(self.secret_word))
            self.prompt_new_game()

    def prompt_new_game(self):
        self.new_game_button = tk.Button(self, text="New Game?", command=self.restart_game)
        self.new_game_button.pack(pady=10)
        self.guess_button.pack_forget()
        self.entry.pack_forget()

    def restart_game(self):
        self.new_game_button.destroy()
        self.guess_button.pack(pady=10)
        self.entry.pack()
        self.new_game()

if __name__ == "__main__":
    app = App()
    app.mainloop()
