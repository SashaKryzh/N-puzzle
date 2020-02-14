def get_direction(board, coord, dir, wall=False):
    if wall == True:
        if dir == "→" and board[coord[0]][coord[1] + 1] == -1:
            dir = "↓"
        elif dir == "↓" and board[coord[0] + 1][coord[1]] == -1:
            dir = "←"
        elif dir == "←" and board[coord[0]][coord[1] - 1] == -1:
            dir = "↑"
        elif dir == "↑" and board[coord[0] - 1][coord[1]] == -1:
            dir = "→"
        return dir
    else:
        if dir == "→" and board[coord[0]][coord[1] + 1] != 0:
            dir = "↓"
        elif dir == "↓" and board[coord[0] + 1][coord[1]] != 0:
            dir = "←"
        elif dir == "←" and board[coord[0]][coord[1] - 1] != 0:
            dir = "↑"
        elif dir == "↑" and board[coord[0] - 1][coord[1]] != 0:
            dir = "→"
        return dir

