import random
plays = ['rock', 'scissors', 'paper']
computer = random.choice(plays)
name = input('Please Input your name ')
count = 0
computer_score = 0
player_score = 0

def game_play():
    global computer_score
    global player_score
    player = input("Rock, paper, scissors? ")
    if computer in ("rock", 'ROCK'):
        if player in ("rock", 'ROCK'):
            print('No one won this play. Play again \n')

    if computer in ('rock', 'ROCK'):
        if player in ('paper', 'PAPER'):
            print(f'{name} won this play. Play again \n')
            player_score += 1

    if computer in ('rock', 'ROCK'):
        if player in ('scissors', 'SCISSORS'):
            print(f'Computer won this play. Play again \n')
            computer_score += 1

    if computer in ('paper', 'PAPER'): 
        if player in ('rock', 'ROCK'):
            print(f'Computer won this play. Play again \n')
            computer_score += 1

    if computer in ('paper', 'PAPER'):
        if player in ('paper', 'PAPER'):
            print('No one won this play. Play again \n')

    if computer in ('paper', 'PAPER'):
        if player in ('scissors', 'SCISSORS'):
            print(f'{name} won this play. Play again \n')
            player_score += 1

    if computer in ('scissors', 'SCISSORS'):
        if player in ('rock', 'ROCK'):
            print(f'{name} won this play. Play again \n')
            player_score += 1

    if computer in ('scissors', 'SCISSORS'):
        if player in ('paper', 'PAPER'):
            print(f'Computer won this play. Play again \n')
            computer_score += 1

    if computer in ('scissors', 'SCISSORS'):
        if player in ('scissors', 'SCISSORS'):
            print('No one won this play. Play again \n')


count = 0
while (count < 3):
        count += 1
        game_play()
        
    
if player_score > computer_score:
    print(f'{name} wins the game!')
    print(f'Computer score : {computer_score}')
    print(f'{name} score : {player_score}')


if computer_score > player_score:
    print(f'Computer wins the game!')
    print(f'Computer score : {computer_score}')
    print(f'{name} score : {player_score}')

if computer_score == player_score:
    print(f'It is a draw!')
    print(f'Computer score : {computer_score}')
    print(f'{name} score : {player_score}')
