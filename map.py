import sys
import time
import random

import pygame
from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT, USEREVENT
from room.lobby import Lobby
from room.roomtypeA import RoomtypeA
from room.escaperoom import EscapeRoom

from character.people import Player
MAX_MAP_TYPE = 2
imgPos = (350, 200)
POSITION = []


def generate_position(imgPos):
    POSITION = []
    Separated_x = -600
    Separated_y = -900
    for i in range(25):
        if i % 5 == 0:
            Separated_x = -600
            Separated_y += 300

        if i == 12:
            POSITION.append(imgPos)
        else:
            POSITION.append((imgPos[0] + Separated_x, imgPos[1] + Separated_y))
        Separated_x += 300
    return POSITION


POSITION = generate_position((350, 200))


class Map:
    def __init__(self, number_of_players):
        pygame.init()
        WINDOW_WIDTH = 1000
        WINDOW_HEIGHT = 700
        BLACK = (0, 0, 0)
        self.window_surface = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('QuickEscape!!')

        self.window_surface.fill(BLACK)

        self.number_of_players = []
        for i in range(number_of_players):
            self.number_of_players.append(Player(
                "picture\\user%s.png" % str(i), (350, 200), 50, 50, "player%s" % str(i+1)))

        self.generate_map()

        __picture = "picture\\stay.jpg"
        __raw_image = pygame.image.load(__picture).convert_alpha()
        self.stay_icon = pygame.transform.scale(
            __raw_image, (125, 125))
        self.stay_icon_rect = self.stay_icon.get_rect()
        self.stay_icon_rect.topleft = (1000 - 125, 700 - 125)

        __picture = "picture\\rotate.jpg"
        __raw_image = pygame.image.load(__picture).convert_alpha()
        self.rotate_icon = pygame.transform.scale(
            __raw_image, (125, 125))
        self.rotate_icon_rect = self.rotate_icon.get_rect()
        self.rotate_icon_rect.topleft = (1000 - 250, 700 - 250)

    def generate_map(self):
        # 大廳的位置 (350, 200)
        # 0代表大廳 1代表出口
        self.map_list = []

        for i in range(25):
            if i == 12:
                self.map_list.append(Lobby(POSITION[i], 200, 200))
            elif i == 7 or i == 11 or i == 13 or i == 17:
                self.map_list.append(
                    RoomtypeA(POSITION[i], 200, 200))
            else:
                self.map_list.append(
                    RoomtypeA(POSITION[i], 200, 200))

        # self.escaoe_index = random.randint(0, 24)
        # while self.escaoe_index == 7 or self.escaoe_index == 11 or self.escaoe_index == 13 or self.escaoe_index == 12 or __escape == 17:
        #     self.escaoe_index = random.randint(0, 24)
        self.escaoe_index = 17
        self.map_list[self.escaoe_index] = EscapeRoom(
            POSITION[self.escaoe_index], 200, 200)
        self.map_list[self.escaoe_index].init_save_player(
            self.number_of_players)

    def print_map(self, imgPos):
        POSITION = generate_position(imgPos)
        for i in range(25):
            self.window_surface.blit(self.map_list[i].image, POSITION[i])
            self.map_list[i].rect.topleft = (POSITION[i][0], POSITION[i][1])

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

        self.move_button = [0] * 4
        # 上
        if self.map_list[__index].gates[0] == 1:
            __rotate_image = pygame.transform.rotate(__image, 90)
            __rect = __rotate_image.get_rect()
            __rect.topleft = (imgPos[0] + remainder, imgPos[1] + quotient)
            self.move_button[0] = __rect
            self.window_surface.blit(
                __rotate_image, (imgPos[0] + remainder, imgPos[1] + quotient))
        # 右
        if self.map_list[__index].gates[3] == 1:
            __rect = __image.get_rect()
            __rect.topleft = (imgPos[0] + remainder +
                              150, imgPos[1] + quotient+150)
            self.move_button[3] = __rect
            self.window_surface.blit(
                __image, (imgPos[0] + remainder+150, imgPos[1] + quotient+150))
        # 下
        if self.map_list[__index].gates[1] == 1:
            __rotate_image = pygame.transform.rotate(__image, -90)
            __rect = __rotate_image.get_rect()
            __rect.topleft = (imgPos[0] + remainder, imgPos[1] + quotient+300)
            self.move_button[1] = __rect
            self.window_surface.blit(
                __rotate_image, (imgPos[0] + remainder, imgPos[1] + quotient+300))
        # 左
        if self.map_list[__index].gates[2] == 1:
            __rotate_image = pygame.transform.rotate(__image, -180)
            __rect = __rotate_image.get_rect()
            __rect.topleft = (imgPos[0] + remainder -
                              150, imgPos[1] + quotient+150)
            self.move_button[2] = __rect
            self.window_surface.blit(
                __rotate_image, (imgPos[0] + remainder-150, imgPos[1] + quotient+150))

    def print_player(self, imgPos, index_of_player):
        __index = self.number_of_players[index_of_player].map_list_position.index(
            1)
        quotient = __index // 5
        remainder = __index % 5
        quotient = 300 * quotient - 600
        remainder = 300 * remainder - 600
        if index_of_player < 3:
            self.window_surface.blit(
                self.number_of_players[index_of_player].image, (imgPos[0]+remainder+75*index_of_player, imgPos[1]+quotient))
        else:
            self.window_surface.blit(
                self.number_of_players[index_of_player].image, (imgPos[0]+remainder+75*(index_of_player-3), imgPos[1]+150+quotient))

    def print_stay(self):
        self.window_surface.blit(
            self.stay_icon, (1000 - 125, 700 - 125))

    def print_rotate(self):
        self.window_surface.blit(
            self.rotate_icon, (1000 - 250, 700 - 250))


if __name__ == '__main__':
    a = Map()
