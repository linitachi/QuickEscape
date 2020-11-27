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
        self.window_surface.blit(self.lobby.image, self.lobby.position)
        self.lobby.numofchars = [1, 0, 0, 0, 0, 0]

        # 讀入RoomtypeA圖片
        self.roomtypeA = RoomtypeA(
            (self.lobby.position[0] - 300, self.lobby.position[1] - 0), 150, 150)
        self.window_surface.blit(self.roomtypeA.image, self.roomtypeA.position)

        # 讀角色圖片

        self.people = People("picture\\user.png", (350, 200), 30, 30, "red")
        self.window_surface.blit(self.people.image, self.people.position)

        pygame.display.update()


if __name__ == '__main__':
    a = Map()
