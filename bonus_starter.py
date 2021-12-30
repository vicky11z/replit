theBoard = []

def emptyBoard():
  return [" "," "," "," "," "," "," "," "," "]

theBoard = emptyBoard()

def numberOrSpace(board,index):
  """
  gives the number or space of a board
  """
  if board[index] != " ":
    return board[index]
  # the display indez is one greater than the actual index
  return str(index + 1)

def rowText(board,row):
  """
  returns a string of a row
  """
  offset = (row - 1) * 3 
  return numberOrSpace(board,offset) + "|" + numberOrSpace(board,offset+1) + "|" + numberOrSpace(board,offset+2)

def printBoard(board):
  """
  This displays the current state of the board
  """
  print("you need to implement printBoard")

def userMove(board,tile):
  """
  This prompts the user for a square and then changes the tile
  of the corresponding square. Remember that lists are index from 0
  so you will have to subtract one to get to the right one.
  """
  print("you need to implement userMove")

print("Getting started.")
print(rowText(theBoard,1))
print(rowText(theBoard,2))