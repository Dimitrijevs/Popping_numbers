def player_turn(board, nums):
    
    rows = len(board)
    cols = len(board[0])
    
    while True:
        try:
            print(f"Available numbers: {nums}")
            num = int(input("Choose a number to place: "))
            if num not in nums:
                raise ValueError("Invalid number. Choose a number in a available range.")
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            row = int(input(f"Choose a row (1-{rows}): ")) - 1
            col = int(input(f"Choose a column (1-{cols}): ")) - 1
            if not (0 <= row < rows and 0 <= col < cols):
                raise ValueError("Invalid position.")
            if board[row][col] not in [" ", "*"]:
                raise ValueError("That position is already taken. Try again.")
            break
        except ValueError as e:
            print(e)

    board[row][col] = num


def check_lines(board):
    player_score = 0

    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] != " ":
                num = board[r][c]

                # Check horizontally
                count = 0
                for i in range(c, len(board[r])):
                    if board[r][i] == num:
                        count += 1
                    else:
                        break
                if count >= 3:
                    player_score += {3: 100, 4: 200, 5: 500}.get(count, 500)
                    for i in range(c, c + count):
                        board[r][i] = " "

                # Check vertically
                count = 0
                for i in range(r, len(board)):
                    if board[i][c] == num:
                        count += 1
                    else:
                        break
                if count >= 3:
                    player_score += {3: 100, 4: 200, 5: 500}.get(count, 500)
                    for i in range(r, r + count):
                        board[i][c] = " "

                # Check diagonally (top-left to bottom-right)
                count = 0
                i, j = r, c
                while i < len(board) and j < len(board[i]):
                    if board[i][j] == num:
                        count += 1
                    else:
                        break
                    i += 1
                    j += 1
                if count >= 3:
                    player_score += {3: 100, 4: 200, 5: 500}.get(count, 500)
                    i, j = r, c
                    for _ in range(count):
                        board[i][j] = " "
                        i += 1
                        j += 1

                # Check diagonally (top-right to bottom-left)
                count = 0
                i, j = r, c
                while i < len(board) and j >= 0:
                    if board[i][j] == num:
                        count += 1
                    else:
                        break
                    i += 1
                    j -= 1
                if count >= 3:
                    player_score += {3: 100, 4: 200, 5: 500}.get(count, 500)
                    i, j = r, c
                    for _ in range(count):
                        board[i][j] = " "
                        i += 1
                        j -= 1

    return player_score
