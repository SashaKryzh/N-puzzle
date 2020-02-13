import sys
from pzl_move0 import move0

def cornerUpRight(brds, x0, y0):
    if (brds.pzl[x0 - 1][y0] != brds.slt[x0 - 1][y0] or
        brds.pzl[x0][y0 + 1] != brds.slt[x0 - 1][y0 + 1] or
        brds.lck[x0 + 1][y0] != 0 or brds.lck[x0 + 1][y0 + 1] != 0):
        print("Can't solve corner !")
        print(brds.pzl)
        print(brds.lck)
        sys.exit()
    tmp1 = brds.pzl[x0 - 1][y0 + 1]
    tmp2 = brds.pzl[x0 + 1][y0 + 1]
    brds.pzl[x0 - 1][y0 + 1] = brds.pzl[x0][y0 + 1]
    brds.pzl[x0 + 1][y0 + 1] = tmp1
    brds.pzl[x0][y0 + 1] = tmp2


def cornerDownRight(brds, x0, y0):
    if (brds.pzl[x0][y0 + 1] != brds.slt[x0][y0 + 1] or
        brds.pzl[x0][y0 + 1] != brds.slt[x0][y0 + 1] or
        brds.lck[x0][y0 - 1] != 0 or brds.lck[x0 + 1][y0 - 1] != 0):
        print("Can't solve corner !")
        print(brds.pzl)
        print(brds.lck)
        sys.exit()
    tmp1 = brds.pzl[x0 + 1][y0 + 1]
    tmp2 = brds.pzl[x0 + 1][y0 - 1]
    brds.pzl[x0 + 1][y0 + 1] = brds.pzl[x0 + 1][y0]
    brds.pzl[x0 + 1][y0 - 1] = tmp1
    brds.pzl[x0 + 1][y0] = tmp2

def cornerDownLeft(brds, x0, y0):
    if (brds.pzl[x0 + 1][y0] != brds.slt[x0 + 1][y0] or
        brds.pzl[x0 + 1][y0] != brds.slt[x0 + 1][y0] or
        brds.lck[x0 - 1][y0] != 0 or brds.lck[x0 - 1][y0 - 1] != 0):
        print("Can't solve corner !")
        print(brds.pzl)
        print(brds.lck)
        sys.exit()
    tmp1 = brds.pzl[x0 + 1][y0 - 1] #14
    tmp2 = brds.pzl[x0 - 1][y0 - 1] #12
    brds.pzl[x0 + 1][y0 - 1] = brds.pzl[x0][y0 - 1]
    brds.pzl[x0 - 1][y0 - 1] = tmp1
    brds.pzl[x0][y0 - 1] = tmp2

def cornerUpLeft(brds, x0, y0):
    if (brds.pzl[x0][y0 - 1] != brds.slt[x0][y0 - 1] or
        brds.pzl[x0][y0 - 1] != brds.slt[x0][y0 - 1] or
        brds.lck[x0][y0 + 1] != 0 or brds.lck[x0 - 1][y0 + 1] != 0):
        print("Can't solve corner !")
        print(brds.pzl)
        print(brds.lck)
        sys.exit()
    tmp1 = brds.pzl[x0 - 1][y0 - 1]
    tmp2 = brds.pzl[x0 - 1][y0 + 1]
    brds.pzl[x0 - 1][y0 - 1] = brds.pzl[x0 - 1][y0]
    brds.pzl[x0 - 1][y0 + 1] = tmp1
    brds.pzl[x0 - 1][y0] = tmp2


def defineCorner(brds):
    x, y = 1, 1
    dir = "→"
    tmp = np.copy(brds.lck)
    while brds.lck[x][y] == 1:
        dir = get_direction(tmp, (x, y), dir, True)
        tmp[x][y] = -1
        if dir == "→":
            y += 1
        elif dir == "↓":
            x += 1
        elif dir == "←":
            y -= 1
        elif dir == "↑":
            x -= 1
    return dir, (x, y)

def solveCornerSituation(brds, cell_nb):
    corner, (x, y) = defineCorner(brds)
    #print(f"Start Corner situation : {corner}, {(x, y)}")
    if corner == '→':
        x0, y0 = x + 1, y - 1
        move0(brds, cell_nb, (x0, y0))
        cornerUpRight(brds, x0, y0)
    elif corner == '↓':
        x0, y0 = x - 1, y - 1
        move0(brds, cell_nb, (x0, y0))
        cornerDownRight(brds, x0, y0)
    elif corner == '←':
        x0, y0 = x - 1, y + 1
        move0(brds, cell_nb, (x0, y0))
        cornerDownLeft(brds, x0, y0)
    elif corner == '↑':
        x0, y0 = x + 1, y + 1
        move0(brds, cell_nb, (x0, y0))
        cornerUpLeft(brds, x0, y0)

