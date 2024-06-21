import random



def check_lines_and_clear(board, r, c, num):
    directions = [
        [(0, 1), (0, -1)],  # Horizontal
        [(1, 0), (-1, 0)],  # Vertical
        [(1, 1), (-1, -1)],  # Diagonal top-left to bottom-right
        [(1, -1), (-1, 1)],  # Diagonal top-right to bottom-left
    ]

    cleared = False
    for direction in directions:
        count = 1
        to_clear = [(r, c)]
        for dr, dc in direction:
            nr, nc = r, c
            while True:
                nr += dr
                nc += dc
                if (
                    0 <= nr < len(board)
                    and 0 <= nc < len(board[0])
                    and board[nr][nc] == num
                ):
                    count += 1
                    to_clear.append((nr, nc))
                else:
                    break

        if count >= 3:
            for cr, cc in to_clear:
                board[cr][cc] = " "
            cleared = True

    return cleared


def enemy_turn(board, nums, enemy_score):
    phrases = [
        "Average Joe is thinking...",
        "Average Joe is making his move...",
        "Average Joe is done.",
        "Average Joe is checking lines...",
        "Average Joe is making a move...",
    ]
    print(random.choice(phrases))

    def place_number(r, c, num):
        board[r][c] = num

    for r in range(len(board)):
        for c in range(len(board[r])):
            num = board[r][c]
            if num != " ":
                # Check horizontally
                for i in range(c + 1, len(board[r])):
                    if board[r][i] == num:
                        if i + 1 < len(board[r]) and board[r][i + 1] == " ":
                            place_number(r, i + 1, num)
                            if check_lines_and_clear(board, r, i + 1, num):
                                enemy_score += 100
                            return enemy_score
                        elif c - 1 >= 0 and board[r][c - 1] == " ":
                            place_number(r, c - 1, num)
                            if check_lines_and_clear(board, r, c - 1, num):
                                enemy_score += 100
                            return enemy_score

                # Check vertically
                for i in range(r + 1, len(board)):
                    if board[i][c] == num:
                        if i + 1 < len(board) and board[i + 1][c] == " ":
                            place_number(i + 1, c, num)
                            if check_lines_and_clear(board, i + 1, c, num):
                                enemy_score += 100
                            return enemy_score
                        elif r - 1 >= 0 and board[r - 1][c] == " ":
                            place_number(r - 1, c, num)
                            if check_lines_and_clear(board, r - 1, c, num):
                                enemy_score += 100
                            return enemy_score

                # Check diagonally (top-right to bottom-left)
                for i, j in zip(range(r + 1, len(board)), range(c - 1, -1, -1)):
                    if board[i][j] == num:
                        if (
                            i + 1 < len(board)
                            and j - 1 >= 0
                            and board[i + 1][j - 1] == " "
                        ):
                            place_number(i + 1, j - 1, num)
                            if check_lines_and_clear(board, i + 1, j - 1, num):
                                enemy_score += 100
                            return enemy_score
                        elif (
                            r - 1 >= 0
                            and c + 1 < len(board[r])
                            and board[r - 1][c + 1] == " "
                        ):
                            place_number(r - 1, c + 1, num)
                            if check_lines_and_clear(board, r - 1, c + 1, num):
                                enemy_score += 100
                            return enemy_score

                # Check diagonally (bottom-right to top-left)
                for i, j in zip(range(r + 1, len(board)), range(c + 1, len(board[r]))):
                    if board[i][j] == num:
                        if (
                            i + 1 < len(board)
                            and j + 1 < len(board[r])
                            and board[i + 1][j + 1] == " "
                        ):
                            place_number(i + 1, j + 1, num)
                            if check_lines_and_clear(board, i + 1, j + 1, num):
                                enemy_score += 100
                            return enemy_score
                        elif i - 1 >= 0 and j - 1 >= 0 and board[i - 1][j - 1] == " ":
                            place_number(i - 1, j - 1, num)
                            if check_lines_and_clear(board, i - 1, j - 1, num):
                                enemy_score += 100
                            return enemy_score

    # If no opportunity to block the player was found, make a random move
    while True:
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board[0]) - 1)
        if board[row][col] == " ":
            selected_num = random.choice(nums)
            board[row][col] = selected_num
            if check_lines_and_clear(board, row, col, selected_num):
                enemy_score += 100  # Add points for clearing
            break

    print(f"Average Joe selected {selected_num}!")
    print(enemy_score)
    return enemy_score
