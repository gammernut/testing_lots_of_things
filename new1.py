# x = ('apple', 'banana', 'cherry')
# y = enumerate(x)
#
# print(dict(y))
#
#
# print(dict(x))


# l1 = ["eat", "sleep", "repeat"]
# s1 = "geek"
#
# # creating enumerate objects
# obj1 = enumerate(l1)
# obj2 = enumerate(s1)
#
# print("Return type:", type(obj1))
# # print(list(enumerate(l1)))
# print(list(enumerate(l1, 1)))
#
# # changing start index to 2 from 0
# print(list(enumerate(s1, 2)))

# import utill
# import random
#
#
# def main():
#     #
#     # main start
#     #
#
#     utill.print_header('Connect Four')
#     # Board is a list of rows
#     # rows are a list of cells
#     board = [
#         [None, None, None, None, None, None, None],
#         [None, None, None, None, None, None, None],
#         [None, None, None, None, None, None, None],
#         [None, None, None, None, None, None, None],
#         [None, None, None, None, None, None, None],
#         [None, None, None, None, None, None, None]
#     ]
#
#     # choose initial player
#     active_player_index = random.randrange(2)
#     # the first player is index/number 0 the second player is index/number 1
#     # ie. player 1 is 0 player 2 is 1
#     # active_player_index = 0
#     players = ["Jacob", "Computer"]
#     symbols = ["X", "O"]
#     player = players[active_player_index]
#     current_player_sym = symbols[active_player_index]
#
#     # test prints
#     print(f'here are the players {players}')
#     print(f'here are the symbols {symbols}')
#     print(f'here is the current player and there symbol {player} {current_player_sym}')
#     # test prints
#
#     announce_turn(player)
#     show_board(board)
# #
# # maine end
# #
#
#
# def show_board(board):
#     for row_idx, row in enumerate(board, start=1):
#         print("| ", end='')
#         for col_idx, cell in enumerate(row, start=1):
#             empty_text = f"({row_idx}, {col_idx})"
#             symbol = f'  {cell}   ' if cell is not None else empty_text
#             print(symbol, end=" | ")
#         print()
#
#
# def announce_turn(player):
#     print()
#     print(f"it is {player}'s turn. Here's the board:")
#     print()
#
#
# if __name__ == '__main__':
#     main()

# board = [
#     # c1   c2    c3    c4     c5    c6    c7
#     [None, None, None, None, None, None, None],  # r1
#
#     # c1   c2    c3    c4     c5    c6    c7
#     [None, None, None, None, None, None, None],  # r2
#
#     # c1   c2    c3    c4     c5    c6    c7
#     [None, None, None, None, None, None, None],  # r3
#
#     # c1   c2    c3    c4     c5    c6    c7
#     [None, None, None, None, None, None, None],  # r4
#
#     # c1   c2    c3    c4     c5    c6    c7
#     [None, None, None, None, None, None, None],  # r5
#
#     # c1   c2    c3    c4     c5    c6    c7
#     [None, None, None, None, None, None, None]  # r6
#     #
# ]
#
#
# def show_board(board):
#     for row_idx, row in enumerate(board, start=1):
#         # print(row_idx, end='')
#         # print(row, end='')
#         print("| ", end='')
#         for col_idx, cell in enumerate(row, start=1):
#             empty_text = f"({row_idx}, {col_idx})"
#             symbol = f'  {cell}   ' if cell is not None else empty_text
#             # print(col_idx, end='')
#             # print(cell, end='')
#             print(symbol, end=" | ")
#         print()
#
#
# show_board(board)


days_var = ['sunday', 'monday', 'tuesday']

for i, days in enumerate(days_var, start=1):
    print(i, days)
