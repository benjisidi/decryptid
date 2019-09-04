import math
import operator
from itertools import product, chain
from functools import reduce

def relative(a, b):
    '''Find the relative coordinates of tiles a and b'''
    return [a[0]-b[0], a[1]-b[1]]

def getAllSigns(*arrays):
    '''
    Return all possible combinations of +ve and -ve list elements
    Concatenates as many lists as you give it

    Example:
        $ getAllSigns([1, 2], [0, 4])
        $ [[1, 2], [-1, 2], [1, -2], [-1, -2], [0, 4], [0, -4]]
    '''
    output = []
    for array in arrays:
        output += list(map(list, product(*([x, -x] if x != 0 else [x] for x in array))))
    return output

def getAbsolutes(tileCoords, relativeCoords):
    '''Given a tile and list of relative coordinates, return all valid absolute tile coordinates'''
    return [[tileCoords[0] + rel[0], tileCoords[1] + rel[1]] for rel in relativeCoords if tileCoords[0] + rel[0] >=0 and tileCoords[1] + rel[1] >=0]

def getAdjacents(tileCoords, order=1):
    '''Get all order-adjacent tiles'''
    relativeCoords = [
        [[0, 0]],
        # Coords of all one-adjacent tiles
        [*getAllSigns([0, 2], [1, 1])],
        # Coords of all two-adjacent tiles
        [*getAllSigns([2, 2], [2, 0], [0, 4], [1, 3])],
        # Coords of all three-adjacent tiles
        [*getAllSigns(*[[x ,x-6] for x in range(4)], [3, 1])]
    ]
    return getAbsolutes(tileCoords, reduce(operator.add, [relativeCoords[i] for i in range(order + 1)], []))

def getTileKey(col, row):
    return f'{col}-{row}'

def getTileCoords(key):
    [x, y] = key.split('-')
    return [int(x), int(y)]

if __name__ == '__main__':
    print(getAdjacents([2, 2], 1))


# Probably won't need this
# def isOneAdjacent(a, b):
#     rel = relative(a, b)
#     return (
#         (rel[0] == 0 and math.fabs(rel[1]) == 2) or 
#         (math.fabs(rel[0]) == 1 and math.fabs(rel[1] == 1))
#     )