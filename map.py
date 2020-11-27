import sys
import time
import random

import pygame
from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT, USEREVENT
from room.lobby import Lobby
from room.roomtypeA import RoomtypeA


class Map:
    def __init__(self):
        pygame.init()
        WINDOW_WIDTH = 800
        WINDOW_HEIGHT = 600
        BLACK = (0, 0, 0)
        self.window_surface = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('QuickEscape!!')
        self.window_surface.fill(BLACK)

        # 讀大廳圖片
        self.lobby = Lobby((350, 200), 150, 150)
        self.window_surface.blit(self.lobby.image, self.lobby.position)

        # 讀入RoomtypeA圖片
        self.roomtypeA = RoomtypeA(
            (self.lobby.position[0] - 300, self.lobby.position[1] - 0), 150, 150)
        self.window_surface.blit(self.roomtypeA.image, self.roomtypeA.position)

        pygame.display.update()


if __name__ == '__main__':
    a = Map()
