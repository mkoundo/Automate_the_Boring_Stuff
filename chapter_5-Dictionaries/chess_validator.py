"""
Ref: Chapter 5 - Dictionaries
Ref: Automate the Boring Stuff with Python, Al Sweigart, 2nd Ed., 2019
Author: Michael Koundouros
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


def isValidChessBoard(piecedict):
    # Check number/colour of pieces are valid
    for colour in ('b', 'w'):
        pieces_list = []
        for value in piecedict.values():
            if value[0] != 'b' and value[0] != 'w': return False  # Check piece colour is valid.
            if value[0] == colour: pieces_list.append(value[1:])
        if not isPieceValid(pieces_list): return False  # Check number of pieces and their names.

    # Check if all piece positions are valid
    board_rows = [1, 2, 3, 4, 5, 6, 7, 8]
    board_cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    all_board_positions = set()
    board_positions = set(piecedict.keys())
    for row in range(8):
        for col in range(8):
            all_board_positions.add(str(board_rows[row]) + board_cols[col])
    return board_positions.issubset(all_board_positions)    # Check position.


def isPieceValid(piece_list):
    # Count number of pieces amd piece names in given piece list are valid.
    piece_dict = {'king': 1, 'queen': 1, 'knight': 2, 'bishop': 2, 'rook': 2, 'pawn': 8}
    board_piece_list = []
    for piece in piece_list:
        if not piece_dict.get(piece, 0): return False   # Check piece name is valid.
    for piece in piece_dict.keys():
        board_piece_list.append(piece_list.count(piece))
        if board_piece_list[-1] > piece_dict[piece]: return False  # Check number of pieces are valid.
    return True


# valid chessboard
chessboard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(chessboard))

# invalid chessboard because invalid colour for item '6e': 'zking'
chessboard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '6e': 'zking'}
print(isValidChessBoard(chessboard))

# invalid chessboard because invalid number of pieces: 2 white queens
chessboard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '6e': 'wqueen'}
print(isValidChessBoard(chessboard))

# invalid chessboard because invalid piece name: '6e': 'wqqueen'
chessboard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '6e': 'wqqueen'}
print(isValidChessBoard(chessboard))
