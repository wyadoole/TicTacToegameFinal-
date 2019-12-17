# one player tic tac toe with AI or player vs AI

# Video post for presintations: https://youtu.be/rbBJnEX7pfk

from random import randint #imports ramdom for randint tp be used
import os# imports os to be used by the game

print("The portion of the final is the PLay vs AI. Where the play play against the AI to win and their is a win condition for only PLayer")# explaining what the fiel does
class AI:# creates the AI
    def __init__(self, board):# takes in itsefl and  board to be used
        self.board = board# gets the board to use

        self.piece = 'O'# set the pieces to O

    def calc_move(self):# calulates the move for the AI
        available_coords = []# tells it what spots are still open to use

        for i in range(len(self.board)):# gets places on the board still open
            for j in range(len(self.board[i])):# gets the array for the AI to place the piece in that place
                if (self.board[i][j] == ' '):# shows the AI that this an open place to put the piece
                    available_coords.append([i, j])# tells it open you can place a piece

        rand_coord = available_coords[randint(0, len(available_coords)-1)]# gets where to choose by radmom guess

        self.board[rand_coord[1]][rand_coord[0]] = 'O'# self of Item place if of O

game = [[' ',' ',' '],  # breaks up the first row into rows 1
        [' ',' ',' '],  # breaks up the first row into rows 2
        [' ',' ',' '],] # breaks up the first row into rows 3

def print_board(board):# prints the board to the user
    print("\t 0 1 2")# y location
    count = 0# set the count to zero -> empty
    for row in board:# checks the row in game if their is a peice
        print(count, end='\t')# prints the board
        for col in row:# columns in row
            print('|' + col, end='')# prints columnbs horizontaly
        print('|')# prints the columns
        count = count + 1# increats the count for the columns after placement

def get_input():# gets the input
    user_input = input("Please enter the coordinates of the position you want to place at as a comma separated list (x, y): ")# tels the user what coordsinates to place and the format

    while len(user_input) > 3:# throughs an exception
        user_input = input("Too many characters. Please enter as a comma separated list ('x, y'): ")# to mmany charecter please reenter for x coordiandtes and y coordaintes

    while (user_input[0] not in '012' and user_input[2] not in '012'):# Throughs an exception
        user_input = input("Invalid input. Please enter as a comma separated list ('x, y'): ")# tell the user invalid inout please reenter again


    return [int(user_input[0]), int(user_input[2])]# return user input

def check_game_over(board):# checks gamevoer condition
    cols = [[],# checks columns 1
            [], # checks colmunsn 2
            []]# checks Columsn 3

    for row in board:# checks the rows
        if len(set(row)) == 1 and row[0] != ' ':# if row not empty then the game is over
            return True# return game winning condition
        else:# then check columns
            cols[0].append(row[0])# Check columns 1
            cols[1].append(row[1])# Check columns 2
            cols[2].append(row[2]) # Check columns 3

    for col in cols:# checks the columns if for win condition
        if len(set(col)) == 1 and col[0] != ' ':# if not emoty then return game is over
            return True# return game winning condition

    diag_1 = [board[0][0], board[1][1], board[2][2]]# check left Daiganal
    diag_2 = [board[0][2], board[1][1], board[2][0]]# check riht Daiganal

    if (len(set(diag_1)) == 1 and diag_1[0] != ' ') or (len(set(diag_2)) == 1 and diag_2[0] != ' '):# check the actual daiganal and is ii three in a row return true game ends
        return True# if true game is over that person wins

    return False# false keep playing

# main loop
def main():
    global game# game is global anyone can call this variable

    playerScore = 0# pkay score is set to zero at game start
    aiScore = 0# AI score its set to zero at gam start

    game_over = False# game is not over start game

    ai = AI(game)# AI goes first

    while (not game_over):# if game is not over
        print_board(game)# print board if not over

        game_over = check_game_over(game)# check win condition
        if not game_over:# if still not won
            inputs = get_input()# enter inout

            game[inputs[1]][inputs[0]] = 'X'# user inout is X
            ai.calc_move()# calucalate move for AI

            os.system('cls')# prints the new baord







if __name__ == '__main__':
    main()# calls main loop