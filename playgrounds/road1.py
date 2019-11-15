from GameLogic.tiles import Tile

def to(pos1, pos2, step = 1):
    p = []
    for i in range(pos1[0], pos2[0] + 1, step):
        for j in range(pos1[1], pos2[1] + 1, step):
            p.append((i, j))
    return p

def add(*pos):
    array = []
    for p in pos:
        for _tuple in p:
            array.append(_tuple)
    return array

road1 = [
    (Tile.BIG_TREE, add(
        to((0, 2), (0, 40), 2),
        to((2, 2), (8, 2), 2),
        to((14, 2), (22, 2), 2),
        to((22, 4), (22, 40), 2),
        to((2, 40), (10, 40), 2),
        to((14, 40), (20, 40), 2)
    ))
]

print(road1)