import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice():
    choice = input("Choose rock, paper, or scissors: ").strip().lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        choice = input("Choose rock, paper, or scissors: ").strip().lower()
    return choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")
    winner = determine_winner(user_choice, computer_choice)
    
    if winner == "draw":
        print("It's a draw!")
    elif winner == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")
    
    return winner

def main():
    print("Welcome to Rock-Paper-Scissors!\n")
    rounds = int(input("How many rounds do you want to play? "))
    
    user_score = 0
    computer_score = 0

    for round_number in range(1, rounds + 1):
        print(f"\nRound {round_number}:")
        winner = play_round()

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"\nScore: You {user_score} - {computer_score} Computer\n")
    
    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif computer_score > user_score:
        print("Sorry, the computer won the game!")
    else:
        print("The game is a draw!")

if __name__ == "__main__":
    main()
