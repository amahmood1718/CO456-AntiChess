import chess

"""Remind me to teach you how to set up a custom board so that you can do your testing"""


#note that player here is the bot
#This function should probably have a while loop which iterates while game is not over
#The function should also read the moves we play as input so we have a back and forth
def play(player):
    return 0

#this function returns the random move to be played
def random_move(board):
    return 0

#returns the set of legal captures, note that legal_moves is in coordinate algebraic notation
def legal_captures(board, legal_moves):
    captures = []
    for x in legal_moves:
        z = chess.parse_square(x[2:])
        if board.piece_at(z) != None:
            captures.append(x)
    return captures


#use this code to convert standard notation to coordinate location
"""
standard_moves = board.legal_moves  
coordinate_moves = []
for x in standard_moves:
    coordinate_moves.append(str(x))
"""
