# this function checks if a queen can be placed in location (col,row)
def isValid(col,row,chessBoard):
  # remove pass and add your code here
  # pass
  '''
  if chessboard[row][col] == 1:
    return False
  '''
  # vertical
  if chessboard[row][0] == 1:
    return False
    
  # horizontal
  if chessboard[0][col] == 1:
    return False
    
  #diagonal
  if chessboard[][]

# initialize chessboard
N = 8
chessBoard = []
for i in range(N):
  chessBoard.append([])
  for j in range(N):
    chessBoard[i].append(0)

# place a queen in the upper left corner of the board
chessBoard[1][1]=1
chessBoard[0][4]=1
chessBoard[2][6]=1

columnIndex = int(raw_input("Enter a column index:"))
rowIndex = int(raw_input("Enter a row index:"))

print ("Placing a queen at column"), columnIndex,("row"), rowIndex,(":"), isValid(columnIndex,rowIndex,chessBoard)