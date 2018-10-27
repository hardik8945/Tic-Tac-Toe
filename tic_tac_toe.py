
#tic tac toc
import numpy

def place_ttt(symbol,board):
    print(numpy.matrix(board))
    while (1):
        row=int(input("Enter row - 1,2,3: "))
        col=int(input("Enter column - 1,2,3: "))
        if (row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-'):
            break
        else:
            print("ENTER CORRECT VALUE!!")

    board[row-1][col-1]=symbol
            
       
    
def check_rows(symbol,board):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count+=1
            if count==3:
                print(symbol, "won")
                return True
    return False

def check_cols(symbol,board):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count+=1
            if count==3:
                print(symbol, "won")
                return False
    return False

def check_diagonals(symbol,board):
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol:
        print(symbol,"won")
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol:
        print(symbol,"won")
        return True
    return True
    
def won_ttt(symbol,board):
    return check_rows(symbol,board) or check_cols(symbol,board) or check_diagonals(symbol,board)

def play_ttt(p1,p2,board):
    for turn in range(9):
        if turn%2==0:
            print("TURN OF x")
            place_ttt(p1,board)
            if won_ttt(p1,board):
                break
        else:
            print("TURN OF o")
            place_ttt(p2,board)
            if won_ttt(p2,board):
                break
        if not(won_ttt(p1,board)) and not(won_ttt(p2,board)):
            print("DRAW")
            

def tic():
    board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
    p1='x'
    p2='o'
    play_ttt(p1,p2,board)
