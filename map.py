import sys
import time
import random

import pygame
from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT, USEREVENT
from room.lobby import Lobby
from room.roomtypeA import RoomtypeA
from character.people import People
MAX_MAP_TYPE = 2


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
        self.generate_map()

    def generate_map(self):
        # 大廳的位置 (350, 200)
        # 0代表大廳 1代表出口
        self.map_list = []
        for i in range(25):
            if i == 12:
                self.map_list.append((0))
            elif i == 7 or i == 11 or i == 13 or i == 17:
                self.map_list.append(random.randint(2, MAX_MAP_TYPE))
            else:
                self.map_list.append(random.randint(2, MAX_MAP_TYPE))
        __escape = random.randint(0, 24)
        while __escape == 7 or __escape == 11 or __escape == 13 or __escape == 12:
            __escape = random.randint(0, 24)
        self.map_list[__escape] = 1

    def print_map(self, imgPos):
        Separated_x = -600
        Separated_y = -900
        for i in range(25):
            if i % 5 == 0:
                Separated_x = -600
                Separated_y += 300
            if self.map_list[i] == 0:
                __image = self.lobby.image
                self.window_surface.blit(__image, imgPos)
            # 出口
            if self.map_list[i] == 1:
                self.window_surface.blit(
                    __image, (imgPos[0] + Separated_x, imgPos[1] + Separated_y))
            # 房間
            if self.map_list[i] == 2:
                __image = self.roomtypeA.image
                self.window_surface.blit(
                    __image, (imgPos[0] + Separated_x, imgPos[1] + Separated_y))

            Separated_x += 300


if __name__ == '__main__':
    a = Map()
