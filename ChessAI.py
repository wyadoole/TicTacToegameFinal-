# 2 player tic tac toe
# youtube playlist for helping get started with the 2 player tic tac toe from Sentdex some of the code is from here to get start from -> https://www.youtube.com/watch?v=eXBD2bB9-RA&list=PLQVvvaa0QuDeAams7fkdcwOGBpGdHpXln
print("This portion of the game is the two player one were each player takes turns trying to beat the other guy boy placing x's or o's on the game board")
import itertools # imports itertools to be used

def win(current_game):#  win condiotn for current game

    def all_same(l):# Sets the win condition to false because all nine places are empty which means all the same
        if l.count(l[0]) == len(l) and l[0] != 0:# if all not O then all are empty
            return True# return true
        else:# esle if not
            return False# return false which mean place have been taken

    # Horizontal
    for row in game:# checks win by horizontal
        print(row)# prints row
        if all_same(row):# checks if all are the same token
            print("Player is the winner Horizontally!(-)")# prints if this play is the winner
            return True# prints true

    # Diagonal
    diags = []#  chcks daigonal of the right
    for col, row, in enumerate(reversed(range(len(game)))):# checks colm and row fro daignaonal
        diags.append(game[row][col])# get sthe daigonal
    if all_same(diags):# if all are the same then prints
        print("Player is the winner diagonal! (/)")# prints the final verdicted then exist the gam e
        return True# game is over if true

    diags = []# chcks daigonal of the right
    for ix in range(len(game)):# checks colm and row fro daignaonal
        diags.append(game[ix][ix])# get sthe daigonal
    if all_same(diags):# if all are the same then prints
        print("Player is the winner diagonal!(\)")# prints the final verdicted then exist the game
        return True# game is over if true

    # Vertical
    for col in range(len(game)):# checks to see all columns ar eth same
        check = []# checks the array

        for row in game:# in game calles check
            check.append(row[col])# check the row for vertical

        if all_same(check):# if all the same
            print("Player is the winner Vertically! (|)")# print winner condiiton
            return True# end game

    return False# if not return false keep playing


# win(game)


def game_board(game_map, player=0, row=0, column=0, just_display=False):# takes in peramter
    try:# through as exception to the game
        print("  0  1  2")# prints locaiton
        if not just_display:# if not deisplayed call the board
            game_map[row][column] = player# check if user error

        for count, row in enumerate(game_map):# checks were it came from from which user
            print(count, row)# prints row
        return game_map# returns map

    except IndexError as e:# throughs an exction
        print("Error: Make your input row as 0 1 2 ?", e)# tell the other error

    except Exception as e:# through an excception
        print("Something went very Wrong!", e)# tell the what the error is
        return False # if not return false ends error exception handleling
#  MAIN LOOP #

play = True# play is true keep playing
players = [1, 2]# tell the game how many players
while play:# when still playing prints this out

# game bord -> below
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0, ]]

    game_won = False# if game won false keep playing
    game = game_board(game, just_display=True)# checks board for win
    player_choice = itertools.cycle([1, 2])# takes turn with each player
    while not game_won:# keep playing
        current_player = next(player_choice)# tell the player and gets the next choice
        print("player", current_player)# tells the user whos up
        column_choice = int(input("What column do you want to play? (0, 1, 2) "))# tells the user what is it row or comn to place the number
        row_choice = int(input("What row do you want to play? (0, 1, 2) "))# tells the user what is it row or comn to place the number
        game = game_board(game, current_player, row_choice, column_choice)# prints game

    if win(game):# end the game
        game_won = True# end the game if this conditionit meet
        again = input("The Game is over, would you like to play again? (y/n) ")# tell the user the game is over do you want to play again
        if again.lower() == "y":# yes is selected
            print("restarting")# game restarts
        elif again.lower() == "n":# no is selected
            print("Bye")# game quits
            play = False# play again is false
        else:
            print("Not a valid answer, so... see you later Aligator")# if not end the game
            play = False #quits the game

game = game_board(game, just_display=True)# keeps track of the board game
game = game_board(game_board, current_player, row=3, column=2)# shows the play where they are and if any oen winning