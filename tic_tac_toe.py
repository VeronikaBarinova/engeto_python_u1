"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Veronika Barinova
email: veronika.barina@gmail.com
discord: veronikabarinova_30716 (not use too much)
"""
from typing import Optional


X = 3 
Y = 3
game_field = [[None for _ in range(X)] for _ in range(Y)]

def print_delimiter(delimiter: str = "="):
    print(delimiter * 45) 

def print_rules():
    print_delimiter()
    print("GAME RULES:")
    print("Each player can place one mark (or stone)")
    print("per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their")
    print("marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print_delimiter()

def print_sep_line():
    for _ in range(3):
        print("+", "-" * 3 , sep="", end="")
    print("+")

def plot_game_field(game_field: list):
    print_delimiter()
    for row in game_field:
        print_sep_line()
        print("|"," | ".join([f"{cell or ' '}" for cell in row]),end=" |\n")

    print_sep_line()
    print_delimiter()

def is_taken(game_field: list, choice: int) -> bool:
    return game_field[(choice - 1) // 3][(choice - 1) % 3] is not None

def ask_player_to_play(Xplayer:bool) -> int:
    print_delimiter()
    while True:
        choice = input(f"Player {'X' if Xplayer else 'O'} | Please enter your move number: ")
        if not choice.isnumeric() or int(choice) not in range(1, 10):
            print("Invalid choice, enter value in 1 to 10")
            continue
        if is_taken(game_field, int(choice)):
            print("Cell is taken, try again..")
            continue
        return int(choice)

def evaluate(game_field: list) -> Optional[str]:
    for row in game_field:
        if row[0] == row[1] == row[2]:
            return row[0]
    for col in range(3):
        if game_field[0][col] == game_field[1][col] == game_field[2][col]:
            return game_field[0][col]
    if game_field[0][0] == game_field[1][1] == game_field[2][2]:
        return game_field[0][0]
    if game_field[0][2] == game_field[1][1] == game_field[2][0]:
        return game_field[0][2]
    return None

def is_full(game_field: list) -> bool:
    return not any(None in row for row in game_field)

if __name__ == "__main__":
    print("Welcome to the TicTacToe")
    print_rules()
    print("Let's start the game")
    print_delimiter("-")
    plot_game_field(game_field)
    Xplay = True
    winner = None
    while (winner := evaluate(game_field)) is None and not is_full(game_field):
        choice = ask_player_to_play(Xplay)
        game_field[(choice - 1) // 3][(choice - 1) % 3] = 'X' if Xplay else 'O'
        plot_game_field(game_field)
        Xplay = not Xplay
    
    if winner is not None:
        print(f"Congratulations, the player {winner}  WON!")
    else:
        print("The game ended in a DRAW!")



