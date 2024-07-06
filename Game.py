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
        self.round_number = 1

        self.create_widgets()
        self.update_score()

    def create_widgets(self):
        self.header_label = tk.Label(self.master, text="Rock-Paper-Scissors", font=("Helvetica", 16))
        self.header_label.pack(pady=10)

        self.round_label = tk.Label(self.master, text=f"Round {self.round_number}", font=("Helvetica", 12))
        self.round_label.pack(pady=5)

        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(pady=10)

        self.rock_button = tk.Button(self.button_frame, text="Rock", command=lambda: self.play_round("rock"))
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = tk.Button(self.button_frame, text="Paper", command=lambda: self.play_round("paper"))
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", command=lambda: self.play_round("scissors"))
        self.scissors_button.grid(row=0, column=2, padx=10)

        self.score_label = tk.Label(self.master, text="", font=("Helvetica", 12))
        self.score_label.pack(pady=10)

        self.reset_button = tk.Button(self.master, text="Restart Game", command=self.reset_game)
        self.reset_button.pack(pady=10)

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

    def play_round(self, user_choice):
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

        messagebox.showinfo("Round Result", f"You chose: {user_choice.capitalize()}\n"
                                            f"Computer chose: {computer_choice.capitalize()}\n\n{result}")

        self.round_number += 1
        self.update_score()

    def update_score(self):
        self.round_label.config(text=f"Round {self.round_number}")
        self.score_label.config(text=f"Score: You {self.user_score} - {self.computer_score} Computer")

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.round_number = 1
        self.update_score()

def main():
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
