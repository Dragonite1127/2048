import pygame
from pygame import transform
import os


class Tile:
    def __init__(self, value, path):
        self.value = value
        self.path = path

    def getValue(self):
        return self.value

    def getPath(self):
        return self.path
class EmptyTile:
    def __init__(self):
        self.value = 0
        self.path = pygame.image.load(os.path.join("assets", "blank.png"))
    def getValue(self):
        return self.value

    def getPath(self):
        return self.path
