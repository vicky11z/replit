def fillBoard():
  """
  Creates a board (list) numbered from 1 - 9.
  """
  board = []
  position = 1
  while position < 10:
    board.append(position)
    position = position + 1
  return board

def printBoard(board):
  """
  Prints out a tic-tac-toe board, given a list.
  """
  print(str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]))
  print(str(board[3]) + " | " + str(board[4]) + " | " + str(board[5]))
  print(str(board[6]) + " | " + str(board[7]) + " | " + str(board[8]))

board = fillBoard()
printBoard(board)

player1 = "X"
player2 = "O"
# Use the current_player variable to determine whose turn it is.
current_player = 1
# Use the number_of_turns variable to create your while loop invariant.
number_of_turns = 0

## YOUR CODE BELOW THIS LINE
