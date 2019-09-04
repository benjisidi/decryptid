import Hex
class Player:
    clues = {}
    def __init__(self, color, clue, board):
        self.color = color
        self.clue = clue
    
    def computeClue(self, board, clue):
        pass
    
    def updateBoard(self, board):
        self.board = board

    def getPossibleSquares(self, color):
        return self.board.getPossibleSquares(color)

    def getOwnSquares(self):
        return self.getPossibleSquares(self.color)
    
    def getOwnPossible(self):
        return self.computeClue(self.clue)

    # ToDo: Add complement (¬) argument and use board.getAllKeys() to get
    def withinNOfFeature(self, n, featureClass, feature, complement, board):
        coordList = set()
        for tileKey in board.getCoords(featureClass, feature) :
            for adjacentTileCoords in Hex.getAdjacents(Hex.getTileCoords(tileKey), n):
                coordList.add(Hex.getTileKey(adjacentTileCoords))
        if (complement):
            allKeys = board.getAllKeys()
            return allKeys - coordList
        return coordList