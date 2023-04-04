import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'tie'
    
    if isWin(user, computer):
        return 'You won! Computer had: ' + computer
    
    return 'Computer had ' + computer + ' You lost :('
    
def isWin(player, opponent):
    if(player =='r' and opponent == 's') or (player == 's' and opponent == 'p')\
        or (player =='p' and opponent == 'r'):
        return True
    
print(play())