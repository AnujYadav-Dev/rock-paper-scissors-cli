import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print("\nYour choice:", user_choice.capitalize())
    print("Computer's choice:", computer_choice.capitalize())
    
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("You lose!")

def get_full_choice(choice):
    # Map single letter input to full choice
    if choice == 'r':
        return 'rock'
    elif choice == 'p':
        return 'paper'
    elif choice == 's':
        return 'scissors'
    return choice  # Return original choice if full word is entered

def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\n--- Rock-Paper-Scissors Game ---")
        print("Current Score -> You: {} | Computer: {}".format(user_score, computer_score))
        
        user_choice = input("Choose (R)ock, (P)aper, or (S)cissors (or 'Q' to quit the game): ").lower().strip()
        
        # Check if the user wants to quit
        if user_choice in ["q", "quit"]:
            print("\nFinal Score -> You: {} | Computer: {}".format(user_score, computer_score))
            print("Thanks for playing!")
            break
        
        # Get the full choice based on single letter or full name input
        user_choice = get_full_choice(user_choice)
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please enter R, P, S, or the full word (rock, paper, scissors).")
            continue
        
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        
        display_result(user_choice, computer_choice, winner)
        
        play_again = input("\nDo you want to play another round? (Y)es or (N)o: ").lower().strip()
        if play_again not in ['y', 'yes']:
            print("\nFinal Score -> You: {} | Computer: {}".format(user_score, computer_score))
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
