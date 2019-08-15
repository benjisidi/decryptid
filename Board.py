from tkinter import Tk, Canvas
from collections import defaultdict
from copy import deepcopy
import math

# ToDo: Clean up namedtuples being duplicated

class Board:
    cos60 = math.cos(math.radians(60))
    sin60 = math.sin(math.radians(60))

    def __init__(self, dims, pieces, pieceOrder, structures = {}, origin = {'x': 100, 'y': 100}):
        self.dims = dims
        self.hexWidth = self.dims['length']*(1+Board.cos60)
        self.hexHeight = self.dims['length'] * Board.sin60
        self.origin = origin
        self.structures = structures
        self.terrainColors = {
            'desert': '#ebc034',
            'swamp': '#3d1254',
            'forest': '#186622',
            'mountain': '#999999',
            'water': '#3c6eba'
        }
        self.territoryColors = {
            'bear': '#000',
            'cougar': '#F00'
        }
        self.terrains = {
            'desert': [],
            'forest': [],
            'mountain': [],
            'swamp': [],
            'water': []
        }
        self.territories = {
            'bear': [],
            'cougar': []
        }
        self.tiles = {}
        self.loadPieces(pieces, pieceOrder)
        for tileKey in structures:
            self.tiles[tileKey]['structure'] = structures[tileKey]

    def rotatePiece(self, piece):
        flippedPiece = deepcopy(piece)
        flip = lambda coord: [int(math.fabs(i - 5)) for i in coord]
        for environment in flippedPiece['terrain']:
            flippedPiece['terrain'][environment] = [flip(tile) for tile in flippedPiece['terrain'][environment]]
        for animal in flippedPiece['territories']:
            flippedPiece['territories'][animal] = [flip(tile) for tile in flippedPiece['territories'][animal]]
        return flippedPiece

    def loadPieces(self, pieces, pieceOrder):
        vertMultiplier = [0, 1, 0, 1, 0, 1]
        horizMultiplier = [0, 0, 1, 1, 2, 2]
        for (i, pieceNumber) in enumerate(pieceOrder):
            index = int(math.fabs(pieceNumber))
            piece = pieces[index]
            if pieceNumber < 0:
                piece = self.rotatePiece(piece)
            for environment in piece['terrain']:
                for tile in piece['terrain'][environment]:
                    tile = [tile[0] + vertMultiplier[i]*6, tile[1] + horizMultiplier[i]*6]
                    tileKey = self.getTileKey(*tile)
                    self.tiles[tileKey] = {'terrain': environment}
                    self.tiles[tileKey]['coords'] = tile
                    self.terrains[environment].append(tileKey)
            for territory in piece['territories']:
                for tile in piece['territories'][territory]:
                    tile = [tile[0] + vertMultiplier[i]*6, tile[1] + horizMultiplier[i]*6]
                    tileKey = self.getTileKey(*tile)
                    self.tiles[tileKey]['territory'] = territory
                    self.territories[territory].append(tileKey)
    
    def getTileKey(self, col, row):
        return f'{col}-{row}'

    def getTile(self, col, row):
        return self.tiles[self.getTileKey(col, row)]

    def indexToCoords(self, col, row):
        return [self.origin['x'] + (col * self.hexWidth), self.origin['y'] + (row * self.hexHeight)]

    def drawStone(self, x, y, r, color, canvas):
        canvas.create_oval([x, y, x + 2*r, y + 2*r], fill=color, outline='#FFF')

    # ToDo: center properly
    def drawShack(self, x, y, r, color, canvas):
        canvas.create_polygon([x + r, y, x, y +2*r, x + 2*r, y + 2*r], fill=color, outline='#FFF')
    
    def drawStructure(self, tile, canvas):
        callbacks = {
            'shack': self.drawShack,
            'stone': self.drawStone
        }
        r = self.dims['length']/2
        [x, y] = self.indexToCoords(*tile['coords'])
        x += self.dims['length']*0.5 - r
        y +=  self.hexHeight - r
        callbacks[tile['structure'][0]](x, y, r, tile['structure'][1], canvas)

    def drawHex(self, x, y, col, row, canvas, fillColor='', outlineColor='#FFF', width=2, length=False):
        if not length:
            length = self.dims['length']
        points = [
            x, y,
            x+length, y,
            x+length+length*Board.cos60, y+length*Board.sin60,
            x+length, y+2*length*Board.sin60,
            x, y+2*length*Board.sin60,
            x-length*Board.cos60, y+length*Board.sin60
        ]
        canvas.create_polygon(points, outline=outlineColor, fill=fillColor, width=2)
        canvas.pack(fill="both", expand=True)


    def drawTile(self, x, y, col, row, canvas, length=False):
        if not length:
            length = self.dims['length']
        tile = self.getTile(col, row)
        # outlineColor = '#FFF' if 'territory' not in tile else self.territoryColors[tile['territory']] 
        fillColor = self.terrainColors[tile['terrain']]
        self.drawHex(x, y, col, row, canvas, fillColor=fillColor)
        if ('structure' in tile):
            self.drawStructure(tile, canvas)
        if ('territory' in tile):
            territoryColor = self.territoryColors[tile['territory']]
            # ToDo: Eliminate magic numbers
            self.drawHex(x + 4, y + 7, col, row, canvas, outlineColor=territoryColor, width=2, length=self.dims['length']- 8)

    def drawBoard(self, width=1280, height=720):
        root = Tk()
        c = Canvas(root, width=width, height=height)
        c.pack(side="top", fill="both", expand=True)
        
        def drawCols(startIndex):
            for col in range(startIndex, self.dims['cols'], 2):
                for row in range(startIndex, self.dims['rows'], 2):
                    self.drawTile(*self.indexToCoords(col, row), col, row, c)
        # Draw the even columns first
        drawCols(0)
        # Now draw the odd columns
        drawCols(1)



        def quit_window(event):
            root.destroy()
        # drawHex(100, 200, 80, c)
        root.bind('<Escape>', quit_window)
        root.mainloop()

