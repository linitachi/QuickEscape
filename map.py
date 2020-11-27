import sys
import time
import random

import pygame
from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT, USEREVENT
from room.lobby import Lobby
from room.roomtypeA import RoomtypeA
from character.people import People


class Map:
    def __init__(self):
        pygame.init()
        WINDOW_WIDTH = 1000
        WINDOW_HEIGHT = 700
        BLACK = (0, 0, 0)
        self.window_surface = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('QuickEscape!!')
        self.window_surface.fill(BLACK)

        # 讀大廳圖片
        self.lobby = Lobby((350, 200), 150, 150)
        self.lobby.numofchars = [1, 0, 0, 0, 0, 0]

        # 讀入RoomtypeA圖片
        self.roomtypeA = RoomtypeA(
            (self.lobby.position[0] - 300, self.lobby.position[1] - 0), 150, 150)

        # 讀角色圖片
        self.people = People("picture\\user.png", (350, 200), 30, 30, "Red")

        self.people2 = People("picture\\user2.png", (400, 200), 30, 30, "Blue")


if __name__ == '__main__':
    a = Map()
