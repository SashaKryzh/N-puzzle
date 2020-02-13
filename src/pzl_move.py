from pzl_cell import Cell
from pzl_corner import *

def chooseGoodMove(boards, cell):
    for x, y in cell.nxt_move:
        if boards.lck[x][y] != 1:
            return (x, y)

def move_puzzle(boards):
    for i in range(1, boards.dim * boards.dim):
        cell = Cell(boards, i, np.where(boards.slt == i))
        while cell.cp != cell.trgt:
            cell.nxt_move = []
            x, y = int(cell.cp[0]), int(cell.cp[1])
            if cell.cp[0] > cell.trgt[0]:
                cell.nxt_move.append((x - 1, y))
            if cell.cp[0] < cell.trgt[0]:
                cell.nxt_move.append((x + 1, y))
            if cell.cp[1] > cell.trgt[1]:
                cell.nxt_move.append((x, y - 1))
            if cell.cp[1] < cell.trgt[1]:
                cell.nxt_move.append((x, y + 1))
            cell.nxt_move = chooseGoodMove(boards, cell)
            cell0 = move0(boards, cell.nb, cell.nxt_move)
            if cell0 != True:
                solveCornerSituation(boards, cell.nb)
            else:
                boards.pzl[x][y] = boards.pzl[cell.nxt_move[0]][cell.nxt_move[1]]
                boards.pzl[cell.nxt_move[0]][cell.nxt_move[1]] = i
                boards.nb_move += 1

            cell.cp = np.where(boards.pzl == i)

        boards.lck[int(cell.trgt[0])][int(cell.trgt[1])] = 1