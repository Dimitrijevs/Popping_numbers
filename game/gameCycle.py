from game.gameStart import level_select, game_start, enemy_select
from game.terminal import clear_screen
from game.board import print_board, print_colorful_board,  create_board, is_board_full
from game.enemy import enemy_turn
from game.computer import computer_turn
from game.player import player_turn, check_lines
from game.prediction import predict_number



def main():
    clear_screen()
    game_start()

    while True:
        level = level_select()

        clear_screen()

        # game variables
        score = 0

        if (level == 1):
            rows = 7
            cols = 7
            nums = [1, 2, 3]
        elif (level == 2 or level == 3 or level == 4):
            if (level == 2):
                 nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            elif (level == 3 or level == 4):
                nums = []
                while True:
                    try:
                        num_total = int(input("How many numbers do you want to play with? (3-9):"))
                        if num_total not in range(3, 10):
                            raise ValueError(
                                "Invalid number. Choose the number again (3-9): "
                            )
                        break
                    except ValueError as e:
                        print(e)
                    
                for i in range(1, num_total+1):
                    nums.append(i)
                
            if (level == 4):
                enemy_select()
                enemy_score = 0
                
            while True:
                try:
                    rows = int(input("Choose the number of rows (5-25): "))
                    if rows not in range(5, 26):
                        raise ValueError(
                            "Invalid number. Choose the number of rows (5-25): "
                        )
                    break
                except ValueError as e:
                    print(e)

            while True:
                try:
                    cols = int(input("Choose the number of cols (5-25): "))
                    if cols not in range(5, 26):
                        raise ValueError(
                            "Invalid number. Choose the number of cols (5-25): "
                        )
                    break
                except ValueError as e:
                    print(e)

        board = create_board(rows, cols)
        print_board(board)

        full_board = is_board_full(board)
        while not full_board:
            # game logic

            if level == 3:
                future_numbers = []
                show_prediction = (
                    input("Do you want to see the prediction? (yes/no): ")
                    .strip()
                    .lower()
                )

                if show_prediction == "yes":
                    future_numbers = predict_number(board)
                    clear_screen()

                    print("Prediction:")
                    print_colorful_board(board)

            while True:
                try:
                    print(f"Available numbers: {nums}")
                    num = int(input("Choose a number to place: "))
                    if num not in nums:
                        raise ValueError(
                            "Invalid number. Choose a number in a available range."
                        )
                    break
                except ValueError as e:
                    print(e)

            while True:
                try:
                    row = int(input(f"Choose a row (1-{rows-0}): ")) - 1
                    col = int(input(f"Choose a column (1-{cols-0}): ")) - 1
                    if not (0 <= row < rows and 0 <= col < cols):
                        raise ValueError("Invalid position.")
                    break
                except ValueError as e:
                    print(e)

            player_turn(board, num, row, col)
            if is_board_full(board):
                break

            if level == 3:
                computer_turn(board, nums, future_numbers)
            else:
                computer_turn(board, nums)
                
            if is_board_full(board):
                break

            if level == 4:
                enemy_score += enemy_turn(board, nums, enemy_score)

            clear_screen()

            print("After checking lines:")

            # points
            score += check_lines(board)
            print(f"Your score: {score} points")

            if level == 4:
                print(f"Average Joe's score: {enemy_score} points")

                if is_board_full(board):
                    break

            print("")

            if level == 3 or level == 4:
                print_colorful_board(board)
            else:
                print_board(board)


        clear_screen()
        
        if(level == 3 or level == 4):
            print_colorful_board(board)
        else:
            print_board(board)
            
        print("Game over!")
        print("The board is full. Your score: ", score)
        
        if level == 4:
            print("Average Joe's score: ", enemy_score)
            if score > enemy_score:
                print("Congratulations! You won!")
            elif score < enemy_score:
                print("You lost! Average Joe won!")
            else:
                print("It's a tie!")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break
