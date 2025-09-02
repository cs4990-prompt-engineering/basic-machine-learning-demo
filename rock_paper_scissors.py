import random
import time
from sklearn import svm

player_history = []
input_data = [[1, 2], [2, 3], [3, 1]]
output_data = [1, 2, 3]


def get_computer_choice():
    if len(player_history) >= 3:
        model = svm.SVC()
        model.fit(input_data, output_data)
        pre_next_choice = model.predict([[player_history[-2], player_history[-1]]])[0]
        if pre_next_choice == 1:
            return 2
        elif pre_next_choice == 2:
            return 3
        else:
            return 1
    else:
        """Generate a random choice for the computer."""
        choices = [1, 2, 3]  # 1=rock, 2=paper, 3=scissors
        return random.choice(choices)

def get_user_choice():
    """Get and validate the user's choice."""
    while True:
        choice = input("\nEnter your choice (r/p/s) or 'q' to quit: ").lower().strip()
        if choice == 'q':
            return 'quit'
        elif choice in ['r', 'p', 's']:
            # Convert single letter to integer
            choice_map = {'r': 1, 'p': 2, 's': 3}
            return choice_map[choice]
        else:
            print("Invalid choice! Please enter 'r', 'p', 's', or 'q' to quit.")

def determine_winner(user_choice, computer_choice):
    # record the user_choice first
    player_history.append(user_choice)
    if len(player_history) >= 3:
        output_data.append(player_history[-1])
        input_data.append([player_history[-3], player_history[-2]])
        print(input_data)
        print(output_data)
    
    """Determine the winner based on the game rules."""
    if user_choice == computer_choice:
        return "tie"
    
    # 1=rock, 2=paper, 3=scissors
    # Rock(1) beats Scissors(3), Paper(2) beats Rock(1), Scissors(3) beats Paper(2)
    if (user_choice == 1 and computer_choice == 3) or \
       (user_choice == 2 and computer_choice == 1) or \
       (user_choice == 3 and computer_choice == 2):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, result):
    """Display the game result in a nice format."""
    # Convert integers back to readable text
    choice_names = {1: 'ROCK', 2: 'PAPER', 3: 'SCISSORS'}
    
    print(f"\n{'='*40}")
    print(f"Your choice: {choice_names[user_choice]}")
    print(f"Computer's choice: {choice_names[computer_choice]}")
    print(f"{'='*40}")
    
    if result == "tie":
        print("🤝 It's a tie!")
    elif result == "user":
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")
    print(f"{'='*40}")

def play_game():
    """Main game loop."""
    print("🎮 Welcome to Rock Paper Scissors!")
    print("Play against the computer and see who wins!")
    
    user_score = 0
    computer_score = 0
    ties = 0
    
    while True:
        print(f"\n📊 Current Score:")
        print(f"   You: {user_score} | Computer: {computer_score} | Ties: {ties}")
        
        user_choice = get_user_choice()
        
        # Check if user wants to quit
        if user_choice == 'quit':
            break
        
        print("\n🤔 Computer is thinking...")
        time.sleep(1)  # Add a small delay for suspense
        
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        display_result(user_choice, computer_choice, result)
        
        # Update scores
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        else:
            ties += 1
    
    # Final score display
    print(f"\n🏁 Final Score:")
    print(f"   You: {user_score} | Computer: {computer_score} | Ties: {ties}")
    
    if user_score > computer_score:
        print("🎊 Congratulations! You are the overall winner!")
    elif computer_score > user_score:
        print("😅 Better luck next time! The computer wins overall.")
    else:
        print("🤝 It's a tie overall! Great game!")
    
    print("\nThanks for playing! 👋")

if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please try running the game again.")
