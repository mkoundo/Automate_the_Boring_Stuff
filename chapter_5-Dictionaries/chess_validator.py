"""
Ref: Chapter 5 - Dictionaries
Ref: Automate the Boring Stuff with Python, Al Sweigart, 2nd Ed., 2019
Author: Michael Koundouros
        michael.koundouros@outlook.com
        July 2020

In this chapter, we used the dictionary value
{'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
to represent a chess board. Write a function named isValidChessBoard() that takes a dictionary argument and returns
True or False depending on if the board is valid.

A valid board will have exactly one black king and exactly one white king. Each player can only have at most
16 pieces, at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t
be on space '9z'. The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn',
'knight', 'bishop', 'rook', 'queen', or 'king'. This function should detect when a bug has resulted in an improper
chess board.
"""


def isValidChessBoard(dict):
    # check number/colour of pieces
    piece_colour = ('b', 'w')
    for colour in piece_colour:
        pieces_list = []
        for value in dict.values():
            if value[0] == colour: pieces_list.append(value[1:])
        if not isPieceValid(pieces_list): return False

    # check if all piece positions are valid
    board_rows = [1, 2, 3, 4, 5, 6, 7, 8]
    board_cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    all_board_positions = set()
    board_positions = set(dict.keys())
    for row in range(8):
        for col in range(8):
            all_board_positions.add(str(board_rows[row]) + board_cols[col])
    return board_positions.issubset(all_board_positions)


def isPieceValid(piece_list):
    piece_dict = {'king': 1, 'queen': 1, 'knight': 2, 'bishop': 2, 'rook': 2, 'pawn': 8}
    # count each piece in the given piece list
    board_piece_list = []
    for piece in piece_dict.keys():
        board_piece_list.append(piece_list.count(piece))
        if board_piece_list[-1] > piece_dict[piece]: return False
    return True


chessboard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

print(isValidChessBoard(chessboard))
