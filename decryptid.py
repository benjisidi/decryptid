from itertools import product
from Board import Board
from collections import namedtuple
from Player import Player

pieces = [
    {}, # There is no piece 0
    # Piece 1
    {
        'terrain': {
            'desert': [
                [2, 4], [3, 3], [3, 5], [4, 4]
            ],
            'forest': [
                [4, 0], [4, 2], [5, 1], [5, 3], [5, 5]
            ],
            'swamp': [
                [0, 2], [0, 4], [1, 3], [1, 5]
            ],
            'water': [
                [0, 0], [1, 1], [2, 0], [2, 2], [3, 1]
            ]
        },
        'territories': {
            'bear': [
                [3, 5], [4, 4]
            ]
        }
    },
    # Piece 2
    {
        'terrain': {
            'desert': [
                [3, 3], [4, 2], [5, 3], [5, 5]
            ],
            'forest': [
                [1, 1], [2, 0], [2, 2], [3, 1], [4, 0], [5, 1]
            ],
            'mountain': [
                [1, 5], [2, 4], [3, 5], [4, 4]
            ],
            'swamp': [
                [0, 0], [0, 2], [0, 4], [1, 3]
            ]
        },
        'territories': {
            'cougar': [
                [0, 0], [1, 1], [2, 0]
            ]
        }
    },
    # Piece 3
    {
        'terrain': {
            'forest': [
                [2, 0], [2, 2], [3, 1], [4, 0]
            ],
            'mountain': [
                [0, 4], [1, 5], [2, 4], [3, 3], [3, 5]
            ],
            'swamp': [
                [0, 0], [0, 2], [1, 1], [1, 3]
            ],
            'water': [
                [4, 2], [4, 4], [5, 1], [5, 3], [5, 5]
            ]
        },
        'territories': {
            'cougar': [
                [0, 2], [0, 4], [1, 3]
            ]
        }
    },
    # Piece 4
    {
        'terrain': {
            'desert': [
                [0, 0], [0, 2], [0, 4],
                [1, 1], [1, 3], [1, 5],
                [2, 4]
            ],
            'mountain': [
                [2, 0], [2, 2], [3, 1], 
                [4, 0], [5, 1]
            ],
            'forest': [
                [3, 5], [4, 4], [5, 5]
            ],
            'water': [
                [3, 3],[4, 2], [5, 3]
            ]
        },
        'territories': {
            'cougar': [
                [5, 3], [5, 5]
            ]
        }
    },
    # Piece 5
    {
        'terrain': {
            'desert': [
                [0, 4], [1, 3], [1, 5], [2, 2]  
            ],
            'mountain': [
                [3, 1], [4, 0], [4, 2], [5, 1], [5, 3]
            ],
            'swamp': [
                [0, 0], [0, 2], [1, 1], [2, 0] 
            ],
            'water': [
                [2, 4], [3, 3], [3, 5], [4, 4], [5, 5]
            ]
        },
        'territories': {
            'bear': [
                [4, 4], [5,3], [5, 5]
            ]
        }
    },
    # Piece 6
    {
        'terrain': {
            'desert': [
                [0, 0], [1, 1]
            ],
            'forest': [
                [4, 2], [5, 1], [5, 3], [5, 5]
            ],
            'mountain': [
                [0, 2], [0, 4], [1, 3]
            ],
            'swamp': [
                [2, 0], [2, 2], [3, 1], [3, 3], [4, 0]
            ],
            'water': [
                [1, 5], [2, 4], [3, 5], [4, 4]
            ]
        },
        'territories': {
            'bear': [
                [0, 0], [0, 2]
            ]
        }
    },
]

structures = {
    '1-3': ['stone', 'white'],
    '7-1': ['stone', 'blue'],
    '10-4': ['shack', 'green'],
    '5-9': ['stone', 'green'],
    '4-12': ['shack', 'white'],
    '11-13': ['shack', 'blue']
}

def validateConfig(pieces):
    requiredCells = [x for x in product(range(0, 5, 2), repeat=2)] + [x for x in product(range(1, 6, 2), repeat=2)]  
    for (i, piece) in enumerate(pieces):
        if i != 0:
            allCells = []
            for environment in piece['terrain']:
                allCells += piece['terrain'][environment]
            for cell in requiredCells:
                if list(cell) not in allCells:
                    print(f'Environment {i} missing cell {cell}')
if __name__ == '__main__':
    validateConfig(pieces)
    test = Board(**{
        'dims': {'cols':12, 'rows':18, 'length':40},
        'pieces': pieces,
        'pieceOrder': [4, -5, 3, -2, 6, 1],
        'structures': structures,
        'origin': {'x': 100, 'y': 50}
    })
    testPlayer = Player('delta', 'blue', test)
    print(
        testPlayer.computeClue(test, {'features': {'cougar', 'bear'}, 'complement': False, 'radius': 0, 'featureClass': 'territories'})
    )
    test.show()
