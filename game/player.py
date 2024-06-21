def player_turn(board, num, row, col):
    if board[row][col] == "*":
        board[row][col] = num
    elif board[row][col] == " ":
        board[row][col] = num
    else:
        print("That position is already taken. Try again.")


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
