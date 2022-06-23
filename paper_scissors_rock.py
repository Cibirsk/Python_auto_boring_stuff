import random, sys

print('ROCK, PAPER, SCISSORS')
wins = 0
losses = 0
ties = 0

while True:
    print(f'{wins} wins, {losses} losses, {ties} ties')

    your_move = input('enter your move: (r)ock (p)aper (s)cissors or q(uit)')
    if your_move == 'r':
        your_move = 'rock'
    elif your_move == 'p':
        your_move = 'paper'
    elif your_move == 's':
        your_move = 'scissors'
    elif your_move == 'q':
        sys.exit()
    else:
        print('bad input, try again')
        continue
    computer_move = random.choice(['rock', 'paper', 'scissors'])

    print(f'{your_move} versus...')
    print(f'{computer_move}')

    if your_move == computer_move:
        print('It\s a tie')
        ties += 1
    elif your_move == 'rock' and computer_move == 'paper':
        print('computer wins')
        losses += 1
    elif your_move == 'rock' and computer_move == 'scissors':
        print('you win')
        wins += 1
    elif your_move == 'paper' and computer_move == 'rock':
        print('you wins')
        wins += 1
    elif your_move == 'paper' and computer_move == 'scissors':
        print('computer wins')
        losses += 1
    elif your_move == 'scissors' and computer_move == 'rock':
        print('computer wins')
        losses += 1
    elif your_move == 'scissors' and computer_move == 'paper':
        print('you win')
        wins += 1