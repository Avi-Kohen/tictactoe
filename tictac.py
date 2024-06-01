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
    if playing in [0,1]:
        playing+=1
    else:
        playing -=1

def change_element():

    while True:
        try:
            usr_inpt = int(input('choose position play '))
        except ValueError:
            print("WRONG, not an integer")
            continue
        if usr_inpt not in range(1,10):
            print("ERROR, not in range")
        else:
            break

    pos = int(usr_inpt) - 1
    board [int((pos)/3)][pos % 3] = symbols[playing]

print_board()
change_element()
print_board()