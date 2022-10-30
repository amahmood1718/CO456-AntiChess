import chess
import random

"""First input (on line 56) is to indicate who is playing!!!!!!!!!!!!!!!!!"""

#The play function is the one that is called to play against the bot
#note that player here is the bot
"""You probably want to print the board somewhere here for testing or not idrc"""
def play(player):

    #first move
    board = chess.Board()
    if player == "white":
        bot_move = random_move(board)
        print(bot_move)
        board.push_san(bot_move)
    move = input()
    board.push_san(move)
    
    #game plays until it is over
    while not (board.is_game_over(claim_draw = True)):
        bot_move = random_move(board)
        print(bot_move)
        board.push_san(bot_move)
        move = input()
        board.push_san(move)

    if board.outcome() == None:
        print("1/2-1/2")
    else:
        print(board.result())
    pass


#this function returns the random move to be played
def random_move(board):
    #convert standard to coordinate
    standard_moves = board.legal_moves  
    coordinate_moves = []
    for x in standard_moves:
        coordinate_moves.append(str(x))
    
    #getting set of captures
    captures = legal_captures(board, standard_moves)

    if len(captures) == 0:
        return random.choice(coordinate_moves)
    else:
        return random.choice(captures)

#returns the set of legal captures
#note that legal_moves is in standard algebraic notation
def legal_captures(board, legal_moves):
    captures = []
    for x in legal_moves:
        if board.is_capture(x):
            captures.append(str(x))
    return captures

play(input())
