from random import randint
print("Let's play rock, paper, scissors!")
print('Best three out of five wins!')
player_wins = 0
computer_wins = 0

while True:
    print(f"Human Score: {player_wins} Computer Score: {computer_wins}")
    rand_num = randint(0,2)
    if player_wins < 3 and computer_wins < 3:
        print('...rock...')
        print('...paper...')
        print('...scissors...')
        player = input('Player, choose rock, paper, or scissors: ').lower()
        if rand_num == 0:
            computer = 'rock'
        elif rand_num == 1:
            computer = 'paper'
        else:
            computer = 'scissors'
        print(f'---Computer plays {computer}---')

        if player == computer:
            print("***It's a tie!***")
        elif player == 'rock':
            if computer == 'scissors':
                print('***Human wins!***')
                player_wins += 1
            else:
                print('***Computer wins!***')
                computer_wins += 1
        elif player == 'paper':
            if computer == 'rock':
                print('***Human wins!***')
                player_wins += 1
            else:
                print('***Computer wins!***')
                computer_wins += 1
        elif player == 'scissors':
            if computer == 'paper':
                print('***Human wins!***')
                player_wins += 1
            else:
                print('***Computer wins!***')
                computer_wins += 1
        elif player != "rock" or "paper" or "scissors":
            print("You did not enter 'rock', 'paper', or 'scissors' correctly. Computer gets 1 point.")
            computer_wins += 1

    elif player_wins == 3:
        print('*****Player wins it all!*****')
        play_again = input('Do you want to play again? (y/n) ')
        if play_again == "y":
            player_wins = 0
            computer_wins = 0
        else:
            print('Thanks for playing!')
            break
    elif computer_wins == 3:
        print('****Computer wins it all!****')
        play_again = input('Do you want to play again? (y/n) ')
        if play_again == "y":
            player_wins = 0
            computer_wins = 0
        else:
            print('Thanks for playing!')
            break