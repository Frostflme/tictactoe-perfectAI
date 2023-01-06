"""Main file, run this to start the game."""

def main():
    """Main function, loops while no one has won."""
    win = False
    board = [['.', '.', '.'],
             ['.', '.', '.'],
             ['.', '.', '.']]
    while not win:
        playerTurn(board)
        enemyTurn(board)
        win = checkState(board)

def playerTurn(boardState: list):
    print("   0  1  2")
    print("0  %s  %s  %s" % (boardState[0][0], boardState[0][1], boardState[0][2]))
    print("1  %s  %s  %s" % (boardState[1][0], boardState[1][1], boardState[1][2]))
    print("2  %s  %s  %s" % (boardState[2][0], boardState[2][1], boardState[2][2]))
    print()
    input("What move do you want to play?  ")

def enemyTurn(boardState: list):
    pass

def checkState(boardState: list):
    """"""
    for row in range(len(boardState)):
        mainTest = boardState[row][row]
        if mainTest != '.':
            if boardState[row][row - 1] == mainTest and boardState[row][row - 2] == mainTest:
                return(checkPlayer(mainTest))
            if boardState[row - 1][row] == mainTest and boardState[row - 2][row] == mainTest:
                return(checkPlayer(mainTest))
            if row == 2:
                if boardState[row - 1][row - 1] == mainTest and boardState[row + 1][row + 1]:
                    return(checkPlayer(mainTest))
    return False

def checkPlayer(char: str):
    if char.lower() == 'x':
        return "Player"
    elif char.lower() == 'o':
        return "AI"
    else:
        return False

def placePiece(char: str, board: list, location: tuple):
    board[location[0]][location[1]] = char