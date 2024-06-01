#VARIABLES

r1 = ['1','2','3']
r2 = ['4','5','6']
r3 = ['7','8','9']

board = [r1,r2,r3]

players =['player1','player2']
playing = 0
symbols = ['X','O']

#FUNCTIONS

def print_board():
    for row in board:
        print(f"|{'|'.join(str(element) for element in row)}|")

def update_player():
    global playing
    if playing == 0:
        playing +=1
    else:
        playing -=1

def change_element():

    while True:
        try:
            usr_inpt = int(input(f'choose position {players[playing]} '))
        except ValueError:
            print("WRONG, not an integer")
            continue
        if usr_inpt not in range(1,10):
            print("ERROR, not in range")
        else:
            break

    pos = int(usr_inpt) - 1
    board [int((pos)/3)][pos % 3] = symbols[playing]

def check_win():
    win_row = [['X','X','X'],['O','O','O']]
    for row in board:
        if row in win_row:
            return False
    for x in range(0,3):
        if [board[0][x],board[1][x],board[2][x]] in win_row:
            return False
    if [board[0][0],board[1][1],board[2][2]] in win_row:
        return False
    if [board[2][2],board[1][1],board[0][0]] in win_row:
        return False
    return True

def game():
    while check_win():
        print_board()
        change_element()
        update_player()
    update_player()
    print(f"GAME OVER, Player {players[playing]} WIN!!!")
    print_board()
    

game()
