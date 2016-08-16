##from tic_tac_toe.exceptions import*
##import exceptions as exc
from exceptions import *



#internal helpers
def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    ##row = position[0]
    ##col = position[1]
    ##fir_li = board[row]
    ##item = fir_li[col]
    ##if item == "-":
      ##  return True
    ##else:
      ##  return False
    ##pass
    return board[position[0]][position[1]] == '-'


def _position_is_valid(position):
    """
    Checks if given position is a valid. To consider a position as valid, it
    must be a two-elements tuple, containing values from 0 to 2.
    Examples of valid positions: (0,0), (1,0)
    Examples of invalid positions: (0,0,1), (9,8), False

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)

    Returns True if given position is valid, False otherwise.
    """
    position_list = [(x,y) for x in range(3) for y in range(3)]
    return position in position_list


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    all_position = [position for i in board for position in i]
    return '-' not in all_position


def _is_winning_combination(board, combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
    """

    for x, y in combination:
        if board[x][y] != player:
            return False
    return True





def _check_winning_combinations(board, player):
    """
    There are 8 posible combinations (3 horizontals, 3, verticals and 2 diagonals)
    to win the Tic-tac-toe game.
    This helper loops through all these combinations and checks if any of them
    belongs to the given player.

    :param board: Game board.
    :param player: One of the two playing players.

    Returns the player (winner) of any of the winning combinations is completed
    by given player, or None otherwise.
    """
    
    
    
    combinations = (
       # horizontals
        ((0,0), (0,1), (0,2)),
         ((1,0), (1,1), (1,2)),
         ((2,0), (2,1), (2,2)),
 
         # verticals
         ((0,0), (1,0), (2,0)),
         ((0,1), (1,1), (2,1)),
         ((0,2), (1,2), (2,2)),
 
         # diagonals
         ((0,0), (1,1), (2,2)),
         ((2,0), (1,1), (0,2)),
         )
    for combination in combinations:
        if _is_winning_combination(board, combination, player):
            return player
    return None
    
    
    pass

def _get_row_strt(row):
    ans = ""
    two_spaces = "  "
    delimiter = "|" 
    ans += row[0] + two_spaces + delimiter;
    ans += two_spaces + row[1] + two_spaces + delimiter;
    ans += two_spaces + row[2]

    return ans

# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    game = {}
    game['player1'] = 'X'
    game['player2'] = 'O'
    game['board'] = []
    empty_board_row = ['-', '-', '-']
    game['board'] = [empty_board_row[:], empty_board_row[:], empty_board_row[:]]
    game['next_turn'] ='X'
    game['winner'] = None
    
    return game
    
    

def get_winner(game):
    """
    Returns the winner player if any, or None otherwise.
    """
    board = game['board']
    players = ('X', 'O')
    for player in players:
        if _check_winning_combinations(board, player):
            return player
            
    return None


def move(game, player, position):
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    print("Start playing")
    board = game['board']
    
    if not _position_is_valid(position):
       raise InvalidMovement('Position out of range.')

    board = game['board']
    next = get_next_turn(game)
    
    if next is None:
        print('fail')
        raise InvalidMovement("Game is over.")
        
    if not _position_is_empty_in_board(position, board):
        raise InvalidMovement("Position already taken.")
        pass
    if game['next_turn'] != player:
        raise InvalidMovement('"' + game["next_turn"] + '"' +" moves next")
    board = game['board']
    board[position[0]][position[1]] = player # move
    next_player = "X"
    if game["next_turn"] == "X":
        next_player = "O"
    game["next_turn"] = next_player
    
    winner = get_winner(game)
    
    if winner is not None:
        #'"X" wins!'
        game["winner"] = winner
        raise GameOver('"' + winner + '"' +' wins!')
    next = get_next_turn(game)
    if next is None:
        raise GameOver("Game is tied!")

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    ##board = game['board']
    ##ans = "\n"
    ##for row in board:
        ##ans += _get

    board = game["board"]
    ans = "\n"
    number =0
    for row in board:
        ans += _get_row_strt(row) + "\n"
        if number != 2:
            ans+= "--------------"
            ans += "\n"
        number +=1

    return ans
def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    if get_winner(game) is not None:
        return None
    board = game["board"]
    for i in range(3):
        for j in range(3):
            if _position_is_empty_in_board((i, j), board):
                return game['next_turn']
    return None
    pass
