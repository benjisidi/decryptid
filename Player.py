class Player:
    def __init__(self, color, clue, board):
        self.color = color
        self.clue = clue
    
    def computeClue(self):
        pass
    
    def updateBoard(self, board):
        self.board = board

    def getPossibleSquares(self, color):
        return self.board.getPossibleSquares(color)

    def getOwnSquares(self):
        return self.getPossibleSquares(self.color)
    
    def getOwnPossible(self):
        return self.computeClue(self.clue)

    