
def minMoves(h, w, h1, w1):
    '''

    :param h: initial high
    :param w: initial width
    :param h1: final high
    :param w1: final width
    :return: min moves to fold paper from initial to final dimentions
    '''
    moves = 0
    # high
    while h - h1 >= h1:
        h = h // 2 + h % 2
        moves += 1
    if h%h1 != 0:
        h -= h%h1
        moves += 1
    # width
    while w - w1 >= w1:
        w = w // 2 + w % 2
        moves += 1
    if w%w1 != 0:
        w -= w%w1
        moves += 1

    return moves

print(minMoves(5, 5, 2, 2))
