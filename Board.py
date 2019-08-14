from tkinter import *
from collections import namedtuple
import math

class Board:
    cos60 = math.cos(math.radians(60))
    sin60 = math.sin(math.radians(60))

    @staticmethod
    def draw_hex(x, y, l, canvas):
        points = [
            x, y,
            x+l, y,
            x+l+l*Board.cos60, y+l*Board.sin60,
            x+l, y+2*l*Board.sin60,
            x, y+2*l*Board.sin60,
            x-l*Board.cos60, y+l*Board.sin60
        ]
        canvas.create_polygon(points, outline='#000', fill='#CC0')
        canvas.pack(fill="both", expand=True)

    def draw(self, origin, dims, width=1280, height=720):
        root = Tk()
        c = Canvas(root, width=width, height=height)
        c.pack(side="top", fill="both", expand=True)
        
        hexWidth = dims.length*(1+Board.cos60)
        hexHeight = 2 * dims.length * Board.sin60
        def drawCols(colOrigin):
            for row in range(0, dims.rows):
                for col in range(0, dims.cols, 2):
                    Board.draw_hex(colOrigin.x + (col * hexWidth), colOrigin.y + (row * hexHeight), dims.length, c)
        # Draw the even columns first
        drawCols(origin)
        # Now draw the odd columns
        Point = namedtuple('Point', ['x', 'y'])
        newOrigin = Point(    
            origin.x + dims.length*(1 + Board.cos60),
            origin.y + dims.length*Board.sin60
        )
        drawCols(newOrigin)



        def quit_window(event):
            root.destroy()
        # draw_hex(100, 200, 80, c)
        root.bind('<Escape>', quit_window)
        root.mainloop()

if __name__ == '__main__':
    Dims = namedtuple('Dims', ['cols', 'rows', 'length'])
    Point = namedtuple('Point', ['x', 'y'])
    test = Board()
    test.draw(Point(100, 100), Dims(6, 3, 80))