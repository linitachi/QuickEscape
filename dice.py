import pygame
import random
dice_icon_size = 125


class Dice:
    def __init__(self, position):
        self.__position = position
        self.test = position
        self.roll_times = 1
        self.__move_times = 0
        self.__rotate_times = 0
        self.init_dice()

    def init_dice(self):
        self.roll_times = 2
        self.__move_times = 0
        self.__rotate_times = 0
        self.roll_dice()
        self.dice_icon_rect = self.dice_icon.get_rect()
        self.dice_icon_rect.topleft = (
            self.__position*dice_icon_size, 700 - dice_icon_size)

    def roll_dice(self):
        if self.roll_times > 0:
            __dice = random.randint(0, 7)
            if __dice < 4:
                __picture = "picture\\dice\\move.png"
                self.__move_times = 1
                self.__rotate_times = 0
            elif __dice < 7:
                __picture = "picture\\dice\\rotate.png"
                self.__rotate_times = 1
                self.__move_times = 0
            else:
                __picture = "picture\\dice\\nothing.png"
                self.__move_times = 0
                self.__rotate_times = 0
            __raw_image_dice = pygame.image.load(__picture).convert_alpha()
            self.dice_icon = pygame.transform.smoothscale(
                __raw_image_dice, (dice_icon_size, dice_icon_size))
            self.roll_times -= 1

    def get_dice_utility(self):
        return self.__move_times, self.__rotate_times
