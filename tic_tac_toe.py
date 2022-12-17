def display_board(board):
    print("+-------" * 3,"+",sep="")
    for row in range(3):
        print("|       " * 3,"|",sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ",end="")
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    
board = [[3* j+ i +1 for i in range(3)]for j in range(3)]
print(board)
display_board(board)

def enter_move(board):
    move = int(input("Enter yout move: "))
    
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    pass

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    pass

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    pass

def draw_move(board):
    # The function draws the computer's move and updates the board.
    pass