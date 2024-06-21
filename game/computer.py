import random


def computer_turn(board, nums, future_numbers = []):
    if future_numbers == []:
        for _ in range(3):
            while True:
                row = random.randint(0, len(board) - 1)
                col = random.randint(0, len(board) - 1)
                if board[row][col] == " ":
                    board[row][col] = random.choice(nums)
                    break
    else:
        for i in range(3):
            row, col = future_numbers[i]
            if board[row][col] != "*":
                continue

            board[row][col] = random.choice(nums)