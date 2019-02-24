
def can_reach(start_coords: tuple = (0, 0), finish_coords: tuple = (0, 0)):
    '''
    INPUT: start_coords(x, y), finish_coords(x, y)
    :param start_coords: X and Y coordinates of start position
    :param finish_coords: X and Y coordinates of finish position
    :return:
    '''
    x1 = start_coords[0]
    y1 = start_coords[1]
    x2 = finish_coords[0]
    y2 = finish_coords[1]

    if x1 > x2 or y1 > y2:
        return 'N'
    mesh = [['N'] * (max(x2, y2) + 1) for pos in range(x2 + 1)]  # create mesh
    mesh[x1][y1] = 'Y'  # set start coords

    for x in range(1, x2 + 1):  # for x
        for y in range(1, y2 + 1):  # for y
            if x - y >= 0 and mesh[x - y][y] == 'Y':
                mesh[x][y] = 'Y'
            elif y - x >= 0 and mesh[x][y - x] == 'Y':
                mesh[x][y] = 'Y'
    for line in mesh[1:]:
        print(line[1:])
    return mesh[x2][y2]


print(can_reach((1, 'o'), (2, 9)))
