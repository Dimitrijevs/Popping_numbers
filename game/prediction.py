import random



def predict_number(board):
    future_numbers = []

    for _ in range(3):
        while True:
            row = random.randint(0, len(board) - 1)
            col = random.randint(0, len(board) - 1)
            if board[row][col] == " ":
                board[row][col] = "*"
                future_numbers.append((row, col))
                break

    return future_numbers
