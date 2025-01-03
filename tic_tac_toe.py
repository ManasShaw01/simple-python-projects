import random

board = [[" "," "," "],[" "," "," "],[" "," "," "]]
PERSON = 'X'
COMPUTER = 'O'

def resetBoard():
    for i in range(3):
        for j in range(3):
            board[i][j] = " "

def showBoard():
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print(f"---+---+---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print(f"---+---+---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")

def isEmpty(row, col):
    if board[row-1][col-1] == " ":
        return True

def isFull():
    emptyspaces = 9
    for i in range(3):
        for j in range(3):
            if board[i][j] != " ":
                emptyspaces -= 1
    return emptyspaces == 0

def personMove():
    x = int(input("Enter the row between (1-3): "))
    y = int(input("Enter the column between (1-3): "))
    if isEmpty(x, y):
        board[x-1][y-1] = PERSON
    else:
        print("That place is already occupied. Try again!")
        personMove()
    return board[x-1][y-1]
    
def computerMove():
    lst = [1,2,3]
    x = random.choice(lst)
    y = random.choice(lst)
    
    print(f"Computer chose row: {x} and column: {y}")
    if isEmpty(x, y):
        board[x-1][y-1] = COMPUTER
    else:
        computerMove()
    return board[x-1][y-1]


# Check if there is a winner
def checkWinner():
    # Check rows and columns for winner
    for i in range(3):
        # Check rows and see if person won
        if board[i][0] == board[i][1] == board[i][2] == PERSON:
            return PERSON
        
        # Check rows and see if computer won
        elif board[i][0] == board[i][1] == board[i][2] == COMPUTER:
            return COMPUTER
        
        # Check columns and see if person won
        elif board[0][i] == board[1][i] == board[2][i] == PERSON:
            return PERSON
        
        # Check columns and see if computer won
        elif board[0][i] == board[1][i] == board[2][i] == COMPUTER:
            return COMPUTER

    # Check diagonals for winner
    if board[0][0] == board[1][1] == board[2][2] == PERSON:
        return PERSON
    elif board[0][0] == board[1][1] == board[2][2] == COMPUTER:
        return COMPUTER
    elif board[0][2] == board[1][1] == board[2][0] == PERSON:
        return PERSON
    elif board[0][2] == board[1][1] == board[2][0] == COMPUTER:
        return COMPUTER
    return " "

def printWinner():
    if checkWinner() == PERSON:
        print("Congratulations! You won!")
    elif checkWinner() == COMPUTER:
        print("You lost! Better luck next time!")
    else:
        print("It's a tie!")


def ticTacToe():
    print("Let's play Tic Tac Toe!")
    print("Here is the board:")
    resetBoard()

    print("*"*20)
    showBoard()
    print("*"*20)

    while not isFull():
        personMove()

        print("*"*20)
        showBoard()
        print("*"*20)

        if checkWinner() != " ":
            printWinner()
            break
        
        computerMove()

        print("*"*20)
        showBoard()
        print("*"*20)

        if checkWinner() != " ":
            printWinner()
            break
    print("Game Over!")
    print("Do you want to play again?")
    playAgain = input("Enter 'yes' or 'no': ")
    if playAgain.lower() == 'yes':
        ticTacToe()
    else:
        print("Thanks for playing!")
    
ticTacToe()