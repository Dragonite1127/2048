import Tile
import pygame
import random
import os
import copy
import main
import time
LAG = 0.025
class Board:
    def __init__(self, dimension, clone):
        self.dimension = dimension
        self.board = self.initBoard()
        self.clone = clone
        self.score = 0

    """Initializes the board where
    each element of the board is 
    an Empty Tile."""
    def initBoard(self):
        board = []
        for k in range(self.dimension):
            board.append([0] * self.dimension)
        for i in range(self.dimension):
            for j in range(self.dimension):
                board[i][j] = Tile.EmptyTile()
        return board

    """Adds a 2 or 4 to a random Empty Tile Location on the board.
    Fails if there is not an empty spot on the Board. """
    def addTwoOrFour(self):
        emptySpot = False
        for row in range(self.dimension):
            for col in range(self.dimension):
                if isinstance(self.board[row][col], Tile.EmptyTile):
                    emptySpot = True
                    break
        if emptySpot:
            choices = [2] * 9 + [4] * 1
            number = random.choice(choices)
            empty = []
            path = pygame.image.load(os.path.join("assets", "2.png")) if number == 2 \
                else pygame.image.load(os.path.join("assets", "4.png"))
            for i in range(self.dimension):
                for j in range(self.dimension):
                    if isinstance(self.board[i][j], Tile.EmptyTile):
                        empty.append([i, j])
            tile = random.choice(empty)
            self.board[tile[0]][tile[1]] = Tile.Tile(number, path)
            self.score += number
    """Returns true if and only if the whole board is occupied by a
    non-empty tile. """
    def boardFull(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if isinstance(self.board[i][j], Tile.EmptyTile):
                    return False
        return True
    """Shifts the contents of the board."""
    def shift(self, direction):
        assert isinstance(direction, str)
        if direction.lower() == "up":
            self.shiftUp()
            self.combineUp()
            self.shiftUp()
        elif direction.lower() == "down":
            self.shiftDown()
            self.combineDown()
            self.shiftDown()
        elif direction.lower() == "left":
            self.shiftLeft()
            self.combineLeft()
            self.shiftLeft()
        elif direction.lower() == "right":
            self.shiftRight()
            self.combineRight()
            self.shiftRight()
        else:
            raise TypeError("Wrong variable type for direction.")
        self.addTwoOrFour()
    """Shifts all tiles up."""
    def shiftUp(self):
        row = 0
        while row <= self.dimension - 1:
            for col in range(self.dimension):
                if isinstance(self.board[row][col], Tile.Tile):
                    tempRow = row
                    while tempRow > 0 and isinstance(self.board[tempRow - 1][col], Tile.EmptyTile): #swaps empty tiles
                        self.swap(tempRow, col, tempRow - 1, col)
                        tempRow -= 1
            row += 1
    def combineUp(self):
        row = 0
        while row <= self.dimension - 1:
            for col in range(self.dimension):
                if isinstance(self.board[row][col], Tile.Tile):
                    tempRow = row
                    while tempRow > 0:
                        if self.board[tempRow - 1][col].value == self.board[tempRow][col].value != 0: #combines values
                            self.changeValue(self.board[tempRow - 1][col], tempRow, col)
                            tempRow -= 1
                        tempRow -= 1
            row += 1
    """Shifts all the tiles down."""
    def shiftDown(self):
        row = self.dimension - 1
        while row >= 0:
            for col in range(len(self.board)):
                if isinstance(self.board[row][col], Tile.Tile):
                    tempRow = row
                    while tempRow < self.dimension - 1:
                        if isinstance(self.board[tempRow + 1][col], Tile.EmptyTile): #swaps empty tiles
                            self.swap(tempRow, col, tempRow + 1, col)
                        tempRow += 1
            row -= 1
    def combineDown(self):
        row = self.dimension - 1
        while row >= 0:
            for col in range(len(self.board)):
                if isinstance(self.board[row][col], Tile.Tile):
                    tempRow = row
                    while tempRow < self.dimension - 1:
                        if self.board[tempRow + 1][col].value == self.board[tempRow][col].value != 0: #combines values
                            self.changeValue(self.board[tempRow + 1][col], tempRow, col)
                            tempRow += 1
                        tempRow += 1
            row -= 1
    """Shifts all the tiles left."""
    def shiftLeft(self):
        row = 0
        while row <= self.dimension - 1:
            col = 0
            while col <= self.dimension - 1:
                if isinstance(self.board[row][col], Tile.Tile):
                    tempCol = col
                    while tempCol > 0 and isinstance(self.board[row][tempCol - 1], Tile.EmptyTile):
                        self.swap(row, tempCol - 1, row, tempCol)
                        tempCol -= 1
                col += 1
            row += 1
    def combineLeft(self):
        row = 0
        while row <= self.dimension - 1:
            col = 0
            while col <= self.dimension - 1:
                if isinstance(self.board[row][col], Tile.Tile):
                    tempCol = col
                    while tempCol > 0:
                        if self.board[row][tempCol - 1].value == self.board[row][tempCol].value != 0:
                            self.changeValue(self.board[row][tempCol - 1], row, tempCol)
                            tempCol -= 1
                        tempCol -= 1
                col += 1
            row += 1

    """Shifts all the tiles right."""
    def shiftRight(self):
        row = self.dimension - 1
        while row >= 0:
            col = self.dimension - 1
            while col >= 0:
                if col != self.dimension - 1 and isinstance(self.board[row][col], Tile.Tile):
                    tempCol = col
                    while tempCol < self.dimension - 1:
                        if isinstance(self.board[row][tempCol + 1], Tile.EmptyTile):
                            self.swap(row, tempCol + 1, row, tempCol)
                        tempCol += 1
                col -= 1
            row -= 1
    """Combines all tiles to the right."""
    def combineRight(self):
        row = self.dimension - 1
        while row >= 0:
            col = self.dimension - 1
            while col >= 0:
                if col != self.dimension - 1 and isinstance(self.board[row][col], Tile.Tile):
                    tempCol = col
                    while tempCol < self.dimension - 1:
                        if self.board[row][tempCol + 1].value == self.board[row][tempCol].value != 0:
                            self.changeValue(self.board[row][tempCol + 1], row, tempCol)
                            tempCol += 1
                        tempCol += 1
                col -= 1
            row -= 1

    """Swaps the position of two squares on the board."""
    def swap(self, a, b, c, d):
        temp = self.board[a][b]
        self.board[a][b] = self.board[c][d]
        self.board[c][d] = temp
        if not self.clone:
            time.sleep(0.01)
            main.draw_window()
            main.drawGrid(self)


    """Returns true if and only if the game is over.
    A game is over when no moves can be made on the board."""
    def gameOver(self):
        boardCopy = Board(main.DIMENSION, True)
        for i in range(self.dimension):
            for j in range(self.dimension):
                boardCopy.board[i][j].value = self.board[i][j].value
                boardCopy.board[i][j].path = self.board[i][j].path
        for direction in ["up", "down", "left", "right"]:
            boardCopy.shift(direction)
        for i in range(self.dimension):
            for j in range(self.dimension):
                boardValue = boardCopy.board[i][j].value
                selfValue = self.board[i][j].value
                if selfValue != boardValue:
                    return False
        return True

    """Changes the value of two tiles.
        @:parameter tile - The tile to change
        @:parameter tileEmpty - The tile to set the empty. """
    def changeValue(self, tile, i, j):
        if tile.value == 2:
            tile.value = 4
            tile.path = pygame.image.load(os.path.join("assets", "4.png"))
        elif tile.value == 4:
            tile.value = 8
            tile.path = pygame.image.load(os.path.join("assets", "8.png"))
        elif tile.value == 8:
            tile.value = 16
            tile.path = pygame.image.load(os.path.join("assets", "16.png"))
        elif tile.value == 16:
            tile.value = 32
            tile.path = pygame.image.load(os.path.join("assets", "32.png"))
        elif tile.value == 32:
            tile.value = 64
            tile.path = pygame.image.load(os.path.join("assets", "64.png"))
        elif tile.value == 64:
            tile.value = 128
            tile.path = pygame.image.load(os.path.join("assets", "128.png"))
        elif tile.value == 128:
            tile.value = 256
            tile.path = pygame.image.load(os.path.join("assets", "256.png"))
        elif tile.value == 256:
            tile.value = 512
            tile.path = pygame.image.load(os.path.join("assets", "512.png"))
        elif tile.value == 1024:
            tile.value = 1024
            tile.path = pygame.image.load(os.path.join("assets", "1024.png"))
        elif tile.value == 2048:
            tile.value = 4096
            tile.path = pygame.image.load(os.path.join("assets", "4096.png"))
        elif tile.value == 4096:
            tile.value = 8192
            tile.path = pygame.image.load(os.path.join("assets", "8192.png"))
        elif tile.value == 8192:
            tile.value = 16384
            tile.path = pygame.image.load(os.path.join("assets", "16384.png"))
        elif tile.value == 16384:
            tile.value = 32768
            tile.path = pygame.image.load(os.path.join("assets", "32768.png"))
        elif tile.value == 32768:
            tile.value = 65536
            tile.path = pygame.image.load(os.path.join("assets", "65536.png"))
        elif tile.value == 65536:
            pass
        else:
            raise ValueError("Error in changeValue function.")
        self.score += tile.value
        self.board[i][j] = Tile.EmptyTile()


