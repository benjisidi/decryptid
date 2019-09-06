import Hex
from operator import itemgetter

class Player:
    clues = {}
    def __init__(self, color, clue, board):
        self.color = color
        self.clue = clue
    
    def updateBoard(self, board):
        self.board = board

    def getPossibleSquares(self, color):
        return self.board.getPossibleSquares(color)

    def getOwnSquares(self):
        return self.getPossibleSquares(self.color)
    
    def getOwnPossible(self):
        return self.computeClue(self.clue)

    def withinNOfFeature(self, n, featureClass, features, complement, board):
        coordList = set()
        for feature in features:
            for tileKey in board.getCoords(featureClass, feature) :
                for adjacentTileCoords in Hex.getAdjacents(Hex.getTileCoords(tileKey), n):
                    coordList.add(Hex.getTileKey(*adjacentTileCoords))
        if (complement):
            allKeys = board.getAllKeys()
            return allKeys - coordList
        return coordList

    def computeClue(self, board, clue):
        featureClass, features, radius, complement = itemgetter('featureClass', 'features', 'radius', 'complement')(clue)
        possibleSquares = self.withinNOfFeature(radius, featureClass, features, complement, board)
        return possibleSquares

