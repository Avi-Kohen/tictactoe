#VARIABLES

r1 = ['1','2','3']
r2 = ['4','5','6']
r3 = ['7','8','9']

board = [r1,r2,r3]

players =['player1','player2']

#FUNCTIONS

def print_board():
    for row in board:
        print(f"|{'|'.join(str(element) for element in row)}|")

def change_element():
    pos = input('choose position play')


print_board()