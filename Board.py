from tkinter import Tk, Canvas
from collections import defaultdict
import math

# ToDo: Clean up namedtuples being duplicated

class Board:
    cos60 = math.cos(math.radians(60))
    sin60 = math.sin(math.radians(60))

    def __init__(self, dims, origin = {'x': 100, 'y': 100}, terrain={}, territories={}, structures={}):
        self.dims = dims
        self.hexWidth = self.dims['length']*(1+Board.cos60)
        self.hexHeight = self.dims['length'] * Board.sin60
        self.origin = origin
        self.terrain = terrain
        self.territories = territories
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
        self.tiles = {}
        # Terrain contains one entry for each tile, so iterate over that and make an entry for each hex, then 
        # update the rest of their attributes
        for environment in terrain:
            for tile in terrain[environment]:
                self.tiles[self.tileKey(*tile)] = {'terrain': environment}
                self.tiles[self.tileKey(*tile)]['coords'] = tile
        for territory in territories:
            for tile in territories[territory]:
                self.tiles[self.tileKey(*tile)]['territory'] = territory
        for tileKey in structures:
            self.tiles[tileKey]['structure'] = structures[tileKey]
    
    def tileKey(self, col, row):
        return f'{col}-{row}'

    def getTile(self, col, row):
        return self.tiles[self.tileKey(col, row)]

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

    def drawHex(self, x, y, col, row, canvas):
        points = [
            x, y,
            x+self.dims['length'], y,
            x+self.dims['length']+self.dims['length']*Board.cos60, y+self.dims['length']*Board.sin60,
            x+self.dims['length'], y+2*self.dims['length']*Board.sin60,
            x, y+2*self.dims['length']*Board.sin60,
            x-self.dims['length']*Board.cos60, y+self.dims['length']*Board.sin60
        ]
        tile = self.getTile(col, row)
        outlineColor = '#FFF' if 'territory' not in tile else self.territoryColors[tile['territory']] 
        fillColor = self.terrainColors[tile['terrain']]
        canvas.create_polygon(points, outline=outlineColor, fill=fillColor, width=2)
        if ('structure' in tile):
            self.drawStructure(tile, canvas)
        canvas.pack(fill="both", expand=True)

    def drawBoard(self, width=1280, height=720):
        root = Tk()
        c = Canvas(root, width=width, height=height)
        c.pack(side="top", fill="both", expand=True)
        
        def drawCols(startIndex):
            for col in range(startIndex, self.dims['cols'], 2):
                for row in range(startIndex, self.dims['rows'], 2):
                    self.drawHex(*self.indexToCoords(col, row), col, row, c)
        # Draw the even columns first
        drawCols(0)
        # Now draw the odd columns
        drawCols(1)



        def quit_window(event):
            root.destroy()
        # drawHex(100, 200, 80, c)
        root.bind('<Escape>', quit_window)
        root.mainloop()

