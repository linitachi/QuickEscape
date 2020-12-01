import sys
import time
import random
from random import choice
import pygame
from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT, USEREVENT
from room.lobby import Lobby
from room.roomtypeA import RoomtypeA
from room.roomtypeB import RoomtypeB
from room.roomtypeC import RoomtypeC
from room.roomtypeD import RoomtypeD

from room.escaperoom import EscapeRoom
from dice import Dice
from character.people import Player

MAX_MAP_TYPE = 2
imgPos = (350, 200)
POSITION = []
stay_icon_size = 125
rotate_icon_size = 125
dice_icon_size = 125
dice_confirm_icon_size = 125


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
            (WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption('QuickEscape!!')

        self.window_surface.fill(BLACK)

        self.player_list = []
        for i in range(number_of_players):
            self.player_list.append(Player(
                "picture\\user%s.png" % str(i), (350, 200), 50, 50, "player%s" % str(i+1)))

        # roomtype_list = [RoomtypeA, RoomtypeB, RoomtypeC, RoomtypeD]
        roomtype_list = [RoomtypeD]
        self.generate_map(roomtype_list)

        self.init_stay_button()
        self.init_rotate_button()
        self.init_dice_confirm_button()

        self.dice_list = [Dice(0), Dice(1), Dice(2)]

    def generate_map(self, roomtype_list):
        # 大廳的位置 (350, 200)
        # 0代表大廳 1代表出口
        self.map_list = []

        for i in range(25):
            if i == 12:
                self.map_list.append(Lobby(POSITION[i], 200, 200))
            else:
                self.map_list.append(
                    choice(roomtype_list)(POSITION[i], 200, 200))

        self.escape_index = random.randint(0, 24)
        while self.escape_index == 7 or self.escape_index == 11 or self.escape_index == 13 or self.escape_index == 12 or self.escape_index == 17:
            self.escape_index = random.randint(0, 24)
        # self.escape_index = 17
        self.map_list[self.escape_index] = EscapeRoom(
            POSITION[self.escape_index], 200, 200)
        self.map_list[self.escape_index].init_save_player(
            self.player_list)

    def print_map(self, imgPos):
        POSITION = generate_position(imgPos)
        for i in range(25):
            self.window_surface.blit(self.map_list[i].image, POSITION[i])
            self.map_list[i].rect.topleft = (POSITION[i][0], POSITION[i][1])

    def print_move_icon(self, player, imgPos):
        # 大廳的位置 (350, 200)
        __index = player.map_list_position

        quotient = __index // 5
        remainder = __index % 5
        quotient = 300 * quotient - 600-75
        remainder = 300 * remainder - 600+75

        __raw_image = pygame.image.load(
            "picture\\next-button.png").convert_alpha()
        __image = pygame.transform.smoothscale(__raw_image, (50, 50))

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
        __index = self.player_list[index_of_player].map_list_position
        quotient = __index // 5
        remainder = __index % 5
        quotient = 300 * quotient - 600
        remainder = 300 * remainder - 600
        if index_of_player < 3:
            self.window_surface.blit(
                self.player_list[index_of_player].image, (imgPos[0]+remainder+75*index_of_player, imgPos[1]+quotient))
        else:
            self.window_surface.blit(
                self.player_list[index_of_player].image, (imgPos[0]+remainder+75*(index_of_player-3), imgPos[1]+150+quotient))

    def player_move_criteria(self, direction, __index):
        # return 下一個房間的index 以及它的開口方向
        # 往上
        if direction == 0 and __index > 4:
            return __index - 5, 1
        # 往下
        elif direction == 1 and __index < 20:
            return __index + 5, 0
        # 往左
        elif direction == 2 and (__index % 5) != 0:
            return __index - 1, 3
        # 往右
        elif direction == 3 and (__index % 5) != 4:
            return __index + 1, 2
        return -1, -1

    def init_stay_button(self):
        __picture = "picture\\stay.png"
        __raw_image = pygame.image.load(__picture).convert_alpha()
        self.stay_icon = pygame.transform.smoothscale(
            __raw_image, (stay_icon_size, stay_icon_size))
        self.stay_icon_rect = self.stay_icon.get_rect()
        self.stay_icon_rect.topleft = (
            1000 - stay_icon_size, 700 - stay_icon_size)

    def print_stay(self):
        x, y = self.window_surface.get_size()
        self.window_surface.blit(
            self.stay_icon, (x - stay_icon_size, y - stay_icon_size))
        self.stay_icon_rect.topleft = (x - stay_icon_size, y - stay_icon_size)

    def init_rotate_button(self):
        __picture = "picture\\rotate.png"
        __raw_image = pygame.image.load(__picture).convert_alpha()
        self.rotate_icon = pygame.transform.smoothscale(
            __raw_image, (rotate_icon_size, rotate_icon_size))
        self.rotate_icon_rect = self.rotate_icon.get_rect()
        self.rotate_icon_rect.topleft = (
            1000 - 2*rotate_icon_size, 700 - rotate_icon_size)

    def print_rotate(self):
        x, y = self.window_surface.get_size()
        self.window_surface.blit(
            self.rotate_icon, (x - 250, y - rotate_icon_size))
        self.rotate_icon_rect.topleft = (x - 250, y - rotate_icon_size)

    def print_dice(self):
        x, y = self.window_surface.get_size()
        __i = 0
        for dice in self.dice_list:
            self.window_surface.blit(
                dice.dice_icon, (__i*dice_icon_size, y - dice_icon_size))
            dice.dice_icon_rect.topleft = (
                __i * dice_icon_size, y - dice_icon_size)
            __i += 1

    def init_dice_confirm_button(self):
        __picture = "picture\\dice\\confirm.png"
        __raw_image = pygame.image.load(__picture).convert_alpha()
        self.dice_confirm_icon = pygame.transform.smoothscale(
            __raw_image, (stay_icon_size, stay_icon_size))
        self.dice_confirm_rect = self.stay_icon.get_rect()
        self.dice_confirm_rect.topleft = (
            dice_confirm_icon_size*3, 700 - dice_confirm_icon_size)

    def print_dice_confirm(self):
        x, y = self.window_surface.get_size()
        self.window_surface.blit(
            self.dice_confirm_icon, (3*dice_confirm_icon_size, y - dice_confirm_icon_size))
        self.dice_confirm_rect.topleft = (
            3 * dice_confirm_icon_size, y - dice_confirm_icon_size)

    def get_all_dice(self):
        __rotate_times = 0
        __move_times = 0
        for i in self.dice_list:
            __move, __rotate = i.get_dice_utility()
            __move_times += __move
            __rotate_times += __rotate
        return __move_times, __rotate_times
