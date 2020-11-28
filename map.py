import sys
import time
import random

import pygame
from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT, USEREVENT
from room.lobby import Lobby
from room.roomtypeA import RoomtypeA
from character.people import Player
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

        self.number_of_players = []
        for i in range(6):
            self.number_of_players.append(Player(
                "picture\\user%s.png" % str(i), (350, 200), 50, 50, "player%s" % str(i+1)))

        # 讀角色圖片
        # self.player = Player("picture\\user0.png", (350, 200), 50, 50, "Red")

        # self.player2 = Player("picture\\user1.png", (425, 200), 50, 50, "Blue")
        self.generate_map()

    def generate_map(self):
        # 大廳的位置 (350, 200)
        # 0代表大廳 1代表出口
        self.map_list = []
        Separated_x = -600
        Separated_y = -900
        for i in range(25):
            if i % 5 == 0:
                Separated_x = -600
                Separated_y += 300
            if i == 12:
                self.map_list.append(Lobby((350, 200), 200, 200))
            elif i == 7 or i == 11 or i == 13 or i == 17:
                self.map_list.append(
                    RoomtypeA((350+Separated_x, 200+Separated_y), 200, 200))
            else:
                self.map_list.append(
                    RoomtypeA((350+Separated_x, 200+Separated_y), 200, 200))
            Separated_x += 300
        # TODO:出口
        # __escape = random.randint(0, 24)
        # while __escape == 7 or __escape == 11 or __escape == 13 or __escape == 12:
        #     __escape = random.randint(0, 24)
        # self.map_list[__escape] = RoomtypeA(
        #     (350+Separated_x, 200+Separated_y), 200, 200)

    def print_map(self, imgPos):
        Separated_x = -600
        Separated_y = -900
        for i in range(25):
            if i % 5 == 0:
                Separated_x = -600
                Separated_y += 300

            if i == 12:
                self.window_surface.blit(self.map_list[i].image, imgPos)
                self.map_list[i].rect.topleft = (imgPos[0], imgPos[1])

            else:
                self.window_surface.blit(
                    self.map_list[i].image, (imgPos[0] + Separated_x, imgPos[1] + Separated_y))
                self.map_list[i].rect.topleft = (
                    imgPos[0]+Separated_x, imgPos[1]+Separated_y)
            Separated_x += 300

    def print_move_icon(self, player, imgPos):
        # 大廳的位置 (350, 200)
        __index = player.map_list_position.index(1)

        quotient = __index // 5
        remainder = __index % 5
        quotient = 300 * quotient - 600-75
        remainder = 300 * remainder - 600+75

        __raw_image = pygame.image.load(
            "picture\\next-button.png").convert_alpha()
        __image = pygame.transform.scale(__raw_image, (50, 50))

        # 上
        if self.map_list[__index].gates[0] == 1:
            __rotate_image = pygame.transform.rotate(__image, 90)
            self.window_surface.blit(
                __rotate_image, (imgPos[0] + remainder, imgPos[1] + quotient))
        # 右
        if self.map_list[__index].gates[3] == 1:
            self.window_surface.blit(
                __image, (imgPos[0] + remainder+150, imgPos[1] + quotient+150))
        # 下
        if self.map_list[__index].gates[1] == 1:
            __rotate_image = pygame.transform.rotate(__image, -90)
            self.window_surface.blit(
                __rotate_image, (imgPos[0] + remainder, imgPos[1] + quotient+300))
        # 左
        if self.map_list[__index].gates[2] == 1:
            __rotate_image = pygame.transform.rotate(__image, -180)
            self.window_surface.blit(
                __rotate_image, (imgPos[0] + remainder-150, imgPos[1] + quotient+150))

    def print_player(self, imgPos, index_of_player):
        if index_of_player < 3:
            self.window_surface.blit(
                self.number_of_players[index_of_player].image, (imgPos[0]+75*index_of_player, imgPos[1]))
        else:
            self.window_surface.blit(
                self.number_of_players[index_of_player].image, (imgPos[0]+75*(index_of_player-3), imgPos[1]+150))


if __name__ == '__main__':
    a = Map()
