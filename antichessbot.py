import chess
import random

"""Remind me to teach you how to set up a custom board so that you can do your testing"""

#The play function is the one that is called to play against the bot
#note that player here is the bot
def play(player):
    #first move
    board = chess.Board()
    if player == "white":
        bot_move = random_move(board)
        board.push_san(bot_move)
    move = input()
    board.push_san(move)
    
    #game plays until it is over
    while not board.is_game_over():
        bot_move = random_move(board)
        board.push_san(bot_move)
        move = input()
        board.push_san(move)
    pass

#this function returns the random move to be played
def random_move(board):
    #convert standard to coordinate
    standard_moves = board.legal_moves  
    coordinate_moves = []
    for x in standard_moves:
        coordinate_moves.append(str(x))
    
    #getting set of captures
    captures = legal_captures(board, coordinate_moves)

    if len(captures) == 0:
        return random.choice(coordinate_moves)
    else:
        return random.choice(captures)

#returns the set of legal captures
#note that legal_moves is in coordinate algebraic notation
def legal_captures(board, legal_moves):
    captures = []
    for x in legal_moves:
        z = chess.parse_square(x[2:4])
        if board.piece_at(z) != None:
            captures.append(x)
    return captures
