# --- Game Board Initialization ---
board = [' ' for x in range(10)] # We use index 1-9 for the board and ignore index 0

# --- Functions ---

def display_board(board):
    """Prints the current state of the board to the console."""
    print('-------------')
    print('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' |')
    print('-------------')
    print('| ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' |')
    print('-------------')
    print('| ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' |')
    print('-------------')

def player_input(player_mark):
    """Asks the current player for their move and validates the input."""
    position = 0
    while position not in range(1, 10) or not is_space_free(position):
        try:
            position = int(input(f'{player_mark}, choose your next position (1-9): '))
        except:
            print("Invalid input. Please enter a number between 1 and 9.")

    return position

def place_marker(board, marker, position):
    """Places the player's marker on the board."""
    board[position] = marker

def is_space_free(position):
    """Checks if a position on the board is empty."""
    return board[position] == ' '

def check_win(board, mark):
    """Checks for all possible winning combinations."""
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the left side
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def check_board_full(board):
    """Checks if the board is full, resulting in a draw."""
    for i in range(1,10):
        if is_space_free(i):
            return False
    return True

def choose_first():
    """Randomly decides which player ('X' or 'O') goes first."""
    import random
    if random.randint(0, 1) == 0:
        return 'O'
    else:
        return 'X'

# --- Main Game Loop ---

def play_game():
    """Main function to run the Tic-Tac-Toe game."""
    print('Welcome to Tic Tac Toe!')
    
    # Reset the global board
    global board
    board = [' '] * 10 
    
    player_mark = 'X'
    turn = choose_first()
    print(f'{turn} will go first!')

    game_on = True
    
    while game_on:
        if turn == 'X':
            # Player 'X' Turn
            display_board(board)
            position = player_input(turn)
            place_marker(board, turn, position)

            if check_win(board, turn):
                display_board(board)
                print(f'Congratulations! {turn} has won the game!')
                game_on = False
            else:
                if check_board_full(board):
                    display_board(board)
                    print('The game is a tie!')
                    game_on = False
                else:
                    turn = 'O'
        else:
            # Player 'O' Turn
            display_board(board)
            position = player_input(turn)
            place_marker(board, turn, position)

            if check_win(board, turn):
                display_board(board)
                print(f'Congratulations! {turn} has won the game!')
                game_on = False
            else:
                if check_board_full(board):
                    display_board(board)
                    print('The game is a tie!')
                    game_on = False
                else:
                    turn = 'X'

# --- Start The Game ---
if __name__ == "__main__":
    while True:
        play_game()
        restart = input('Do you want to play again? Enter Yes or No: ').lower()
        if restart[0] == 'n':
            break