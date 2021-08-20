# Rock Paper Scissors!

import random

computer_score = 0
user_score = 0

print("Let's play Rock Paper Scissors! \nBest 2 of 3 games!")

while True:
    user_move = input("Enter your move! (Rock Paper or Scissors)")
    computer_choices = ("rock", "paper", "scissors")
    computer_move = random.choice(computer_choices)

    print(f'You selected {user_move} and the computer selected {computer_move}!')

    if user_move == computer_move:
        print(f'Tie game! You both selected {user_move}. Try again! ')
    elif user_move.lower() == "rock":
        if computer_move == "paper":
            print(f'You lose! The computer selected {computer_move}, {computer_move} covers rock! ')
            computer_score+=1
            if computer_score == 2:
                print(f'Game Over! Final score: Computer: {computer_score} User: {user_score} ')
                computer_score = 0
                user_score = 0
                break
        else:
            print(f'You win! {user_move} smashes {computer_move}! ')
            user_score+=1
            if user_score == 2:
                print(f'Congratulations! You win! Final score: User: {user_score} Computer: {computer_score}!')
                computer_score = 0
                user_score = 0
                break
    elif user_move.lower() == "paper":
        if computer_move == "scissors":
            print(f'You lose! The computer selected {computer_move}, {computer_move} cuts {user_move}! ')
            computer_score+=1
            if computer_score == 2:
                print(f'Game Over! Final score: Computer: {computer_score} User: {user_score} ')
                computer_score = 0
                user_score = 0
                break
        else:
            print(f'You win! {user_move} covers {computer_move}! ')
            user_score+=1
            if user_score == 2:
                print(f'Congratulations! You win! Final score: User: {user_score} Computer: {computer_score}!')
                computer_score = 0
                user_score = 0
                break
    elif user_move.lower() == 'scissors':
        if computer_move == 'rock':
            print(f'You lose! The computer selected {computer_move}, {computer_move} smashes {user_move}! ')
            computer_score+=1
            if computer_score == 2:
                print(f'Game Over! Final score: Computer: {computer_score} User: {user_score} ')
                computer_score = 0
                user_score = 0
                break
        else:
            print(f'You win! {user_move} cuts {computer_move}! ')
            user_score+=1
            if user_score == 2:
                print(f'Congratulations! You win! Final score: User: {user_score} Computer: {computer_score}!')
                computer_score = 0
                user_score = 0
                break

    

