import pygame
from pygame import *

MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR = "#888888"
class Player(sprite.Spite):
    def __init__(self, x, y):
        sprite.Spite.__init__(self)
        self.xvel = 0 #скорость перемещения. 0 - стоять на месте
        self.startX= x
        self.startY = y
        self.image = Surface(WIDTH,HEIGHT)