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


def enemy_turn(board, nums):
    enemy_score = 0
    phrases = [
        "Average Joe is thinking...",
        "Average Joe is making his move...",
        "Average Joe is done.",
        "Average Joe is checking lines...",
        "Average Joe is making a move...",
    ]
    print(random.choice(phrases))

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == " ":
                # Check if placing a number here would complete a line
                for num in nums:
                    board[row][col] = num
                    if check_lines_and_clear(board, row, col, num):
                        # This move would complete a line, so make it
                        print(
                            f"Average Joe placed number {num} at row {row + 1}, column {col + 1} \n"
                        )
                        enemy_score += 100  # Add points for clearing
                        return enemy_score
                    else:
                        # This move wouldn't complete a line, so undo it
                        board[row][col] = " "
    # If no opportunity to complete a line was found, make a random move
    while True:
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board[0]) - 1)
        if board[row][col] == " ":
            selected_num = random.choice(nums)
            board[row][col] = selected_num
            if check_lines_and_clear(board, row, col, selected_num):
                enemy_score += 100  # Add points for clearing
            break
    print(
        f"Average Joe placed number {selected_num} at row {row + 1}, column {col + 1} \n"
    )
    return enemy_score
