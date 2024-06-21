from colorama import Fore, Style



def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def create_board(rows, cols):
    board = []
    for i in range(rows):
        board.append([" "] * cols)
    return board


def print_board(board):
    for row in board:
        # Print the horizontal separator
        for _ in row:
            print("----", end="")
        print("----")

        # Print the cells in the row
        for cell in row:
            if cell == " ":
                print("|   ", end="")
            else:
                print("| " + str(cell) + " ", end="")
        print("|")

    # Print the final horizontal separator
    for _ in board[0]:
        print("----", end="")
    print("----")


def print_colorful_board(board):
    for row in board:
        # Print the horizontal separator
        for _ in row:
            print("----", end="")
        print("----")

        # Print the cells in the row
        for cell in row:
            if cell == " ":
                print("|   ", end="")
            elif cell == 1:
                print("| " + Fore.RED + str(cell) + Style.RESET_ALL + " ", end="")
            elif cell == 2:
                print("| " + Fore.GREEN + str(cell) + Style.RESET_ALL + " ", end="")
            elif cell == 3:
                print("| " + Fore.YELLOW + str(cell) + Style.RESET_ALL + " ", end="")
            elif cell == 4:
                print("| " + Fore.BLUE + str(cell) + Style.RESET_ALL + " ", end="")
            elif cell == 5:
                print("| " + Fore.MAGENTA + str(cell) + Style.RESET_ALL + " ", end="")
            elif cell == 6:
                print("| " + Fore.CYAN + str(cell) + Style.RESET_ALL + " ", end="")
            elif cell == 7:
                print("| " + Fore.WHITE + str(cell) + Style.RESET_ALL + " ", end="")
            elif cell == 8:
                print(
                    "| " + Fore.LIGHTRED_EX + str(cell) + Style.RESET_ALL + " ", end=""
                )
            elif cell == 9:
                print(
                    "| " + Fore.LIGHTBLACK_EX + str(cell) + Style.RESET_ALL + " ",
                    end="",
                )
            else:
                print("| " + str(cell) + " ", end="")
        print("|")

    # Print the final horizontal separator
    for _ in board[0]:
        print("----", end="")
    print("----")
