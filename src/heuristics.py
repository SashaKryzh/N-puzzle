
def manhattan_distance(board, goal):
    board_flat = [item for sublist in state for item in sublist]
    goal_flat = range(0, len(flat_statelist))
    mandistance = 0

    # We use it's modular arthmetic to get it's x and y coordinates in the grid. The manhattan distance is the sum of all these x
    # and y coordinates for each of the tiles
    for element in flat_statelist:
        distance = abs(flat_goallist.index(element) - flat_statelist.index(element))
        xcoord, ycoord = distance // len(state[0]), distance % len(state[0])
        mandistance += xcoord + ycoord
    return mandistance