import random

def get_computer_choice():
    return random.choice(['paper', 'rock', 'scissors'])

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Try again!!')
        return "It's a tie!"
    elif (user_choice == 'scissors' and computer_choice == 'rock') or \
         (user_choice == 'paper' and computer_choice == 'scissors') or \
         (user_choice == 'rock' and computer_choice == 'paper'):
        print('Congratulation🎉🎉')
        return 'You win!'
    else:
        print('All The Best!!')
        return 'Computer wins!'
        
def play_round():
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    result = winner(user_choice, computer_choice)
    print(result)
    return result

def play_game():
    user_score = 0
    computer_score = 0
    play_again = 'yes'
    
    while play_again.lower() in ['yes', 'y']:
        result = play_round()
        if result == 'You win!':
            user_score += 1
        elif result == 'Computer wins!':
            computer_score += 1
        
        print(f"Scores - You: {user_score}, Computer: {computer_score}")
        play_again = input("Do you want to play another round? (yes/no): ")
    
    print("Thanks for playing!")

play_game()
