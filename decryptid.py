from Board import Board
from collections import namedtuple

pieces = [
    {}, # There is no piece 0
    {},
    {},
    {},
    {
        'terrain': {
            'desert': [
                [0, 0], [0, 2], [0, 4],
                [1, 1], [1, 3], [1, 5],
                [2, 4]
            ],
            'mountain': [
                [2, 0], [2, 2],
                [3, 1], 
                [4, 0],
                [5, 1]
            ],
            'water': [
                [3, 3],
                [4, 2],
                [5, 3]
            ],
            'forest': [
                [3, 5],
                [4, 4],
                [5, 5]
            ]
        },
        'territories': {
            'cougar': [
                [5, 3],
                [5, 5]
            ]
        },
        'structures': {
            '5-3': ['shack', 'blue'],
            '5-5': ['shack', 'blue'],
            '4-0': ['stone', 'red']
        }
    }
]

if __name__ == '__main__':
    test = Board(**{
        'dims': {'cols':6, 'rows':6, 'length':80},
        'terrain': pieces[4]['terrain'],
        'territories': pieces[4]['territories'],
        'structures': pieces[4]['structures']
    })
    test.drawBoard()