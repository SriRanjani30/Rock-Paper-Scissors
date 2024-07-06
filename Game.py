import random
import tkinter as tk
from tkinter import messagebox

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock-Paper-Scissors Game")

        self.choices = ["rock", "paper", "scissors"]

        self.user_score = 0
        self.computer_score = 0

        self.label = tk.Label(master, text="Choose rock, paper, or scissors:")
        self.label.pack()

        self.choice_var = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.choice_var)
        self.entry.pack()

        self.play_button = tk.Button(master, text="Play", command=self.play_round)
        self.play_button.pack()

        self.score_label = tk.Label(master, text=f"Score: You {self.user_score} - {self.computer_score} Computer")
        self.score_label.pack()

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "draw"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            return "user"
        else:
            return "computer"

    def play_round(self):
        user_choice = self.choice_var.get().strip().lower()
        if user_choice not in self.choices:
            messagebox.showerror("Error", "Invalid choice. Please choose rock, paper, or scissors.")
            return

        computer_choice = self.get_computer_choice()

        winner = self.determine_winner(user_choice, computer_choice)

        if winner == "draw":
            result = "It's a draw!"
        elif winner == "user":
            result = "You win this round!"
            self.user_score += 1
        else:
            result = "Computer wins this round!"
            self.computer_score += 1

        messagebox.showinfo("Round Result", f"Computer chose: {computer_choice.capitalize()}\n{result}")

        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Score: You {self.user_score} - {self.computer_score} Computer")

def main():
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
