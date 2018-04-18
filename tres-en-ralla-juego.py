#!/usr/bin/python

whostarts = "x"
game_status = "start"

board = [" " for i in range(9)]


def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])
    print(row1)
    print(row2)
    print(row3)

def player_plays(icon):
    choice = int(input("{} player plays, what is your choice (1-9)?:".format(icon)))
    while board[choice -1] != " ":
        print("That space is taken, please repetat")
        choice = int(input("{} player plays, what is your choice (1-9)?:".format(icon)))
    board[choice -1] = icon


def is_victory(icon):
   if (board[0] == icon and  board[1] == icon and board[2] == icon) or \
      (board[3] == icon and  board[4] == icon and board[5] == icon) or \
      (board[6] == icon and  board[6] == icon and board[8] == icon) or \
      (board[0] == icon and  board[3] == icon and board[6] == icon) or \
      (board[1] == icon and  board[4] == icon and board[7] == icon) or \
      (board[2] == icon and  board[5] == icon and board[8] == icon) or \
      (board[0] == icon and  board[4] == icon and board[8] == icon) or \
      (board[2] == icon and  board[4] == icon and board[6] == icon):
        print("{} WINS!".format(icon))
        return(True)


while True:
    print_board()
    player_plays("x")
    if is_victory("x"):
        break
    print_board()
    player_plays("o")
    if is_victory("o"):
        break
