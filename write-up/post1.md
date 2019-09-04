# Decryptid: Building a board-game AI

## Episode 1: set-up

Blah blah some stuff

![board_1](C:\Users\benji.sidi\Documents\personal\decryptid\reference\board_1.jpg)

```python
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
```

