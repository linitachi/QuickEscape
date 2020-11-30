import pygame
import random
dice_icon_size = 125


class Dice:
    def __init__(self, position):
        self.__position = position
        self.test = position
        self.init_dice()

    def init_dice(self):
        __picture = "picture\\dice\\move.png"
        __raw_image = pygame.image.load(__picture).convert_alpha()
        self.dice_icon = pygame.transform.scale(
            __raw_image, (dice_icon_size, dice_icon_size))
        self.dice_icon_rect = self.dice_icon.get_rect()
        self.dice_icon_rect.topleft = (
            self.__position*dice_icon_size, 700 - dice_icon_size)

    def roll_dice(self):
        __dice = random.randint(0, 6)
        if __dice < 3:
            __picture = "picture\\dice\\move.png"
        elif __dice < 5:
            __picture = "picture\\dice\\rotate.png"
        else:
            __picture = "picture\\dice\\nothing.png"
        __raw_image_dice = pygame.image.load(__picture).convert_alpha()
        self.dice_icon = pygame.transform.smoothscale(
            __raw_image_dice, (dice_icon_size, dice_icon_size))

    def test(self):
        print(self.__position)
