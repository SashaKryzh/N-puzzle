from pzl_cell import Cell, np

def chooseGoodDirection(boards, cell):
    #print(f"Choose good direction for {cell.nb} parmis {cell.nxt_move}")

    good_dir = (0, 0)
    best_distance = boards.dim ** 2
    for move in cell.nxt_move:
        distance = abs(move[0] - cell.trgt[0]) + abs(move[1] - cell.trgt[1])
        if distance < best_distance and boards.lck[move[0]][move[1]] != 1:
            best_distance = distance
            good_dir = move
        elif distance == best_distance and boards.lck[move[0]][move[1]] != 1 and cell.tmp_direction == 0:
            cell.tmp_board = np.copy(boards.pzl)
            cell.tmp_direction = move
        #On peut aussi choisir si l'un des deux est un chiffre déjà bien placé
        #ou si les suivants sont déjà placé
    for lst_move in cell.last_move:
        if good_dir == lst_move and cell.tmp_direction != 0 and cell.tmp_direction != -1:
            boards.pzl = cell.tmp_board
            good_dir = cell.tmp_direction
            cell.tmp_direction = -1
            return good_dir
        elif good_dir == lst_move:
            return False
    if good_dir == (0, 0) and cell.tmp_direction != 0 and cell.tmp_direction != -1:
            boards.pzl = cell.tmp_board
            good_dir = cell.tmp_direction
            cell.tmp_direction = -1
            return good_dir
    elif good_dir == (0, 0): #corner situation
        return False
    return good_dir


def move0(boards, cell_nb, target):
    #print(f"On veut placer 0 a la place de : {boards.pzl[target[0]][target[1]]}")
    cell0 = Cell(boards, 0, target)
    while cell0.cp != target:
        cell0.nxt_move = []
        x, y = int(cell0.cp[0]), int(cell0.cp[1])
        if (x + 1, y) != cell0.last_move[-1] and boards.pzl[x + 1][y] != -1 and boards.pzl[x + 1][y] != cell_nb:
            cell0.nxt_move.append((x + 1, y))
        if (x - 1, y) != cell0.last_move[-1] and boards.pzl[x - 1][y] != -1 and boards.pzl[x - 1][y] != cell_nb:
            cell0.nxt_move.append((x - 1, y))
        if (x, y + 1) != cell0.last_move[-1] and boards.pzl[x][y + 1] != -1 and boards.pzl[x][y + 1] != cell_nb:
            cell0.nxt_move.append((x, y + 1))
        if (x, y - 1) != cell0.last_move[-1] and boards.pzl[x][y - 1] != -1 and boards.pzl[x][y - 1] != cell_nb:
            cell0.nxt_move.append((x, y - 1))
        cell0.nxt_move = chooseGoodDirection(boards, cell0)
        cell0.cp = np.where(boards.pzl == 0)
        x, y = int(cell0.cp[0]), int(cell0.cp[1])
        if cell0.nxt_move == False:
            return cell0
        else:
            cell0.last_move.append((x, y))
            boards.pzl[x][y] = boards.pzl[cell0.nxt_move[0]][cell0.nxt_move[1]]
            boards.pzl[cell0.nxt_move[0]][cell0.nxt_move[1]] = 0
            boards.nb_move += 1
        cell0.cp = np.where(boards.pzl == 0)
    return True




