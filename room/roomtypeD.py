from room import Room
import pygame
import random

# 直線的房間，且進入者還可以多一次移動房間的機會


class RoomtypeD(Room):
    def __init__(self, position=(150, 150), width=250, height=250):
        super().__init__(position, width, height)
        self.gates = [1, 1, 0, 0]
        self.__picture = "picture\\roomD.jpg"
        self.raw_image = pygame.image.load(self.back_picture).convert_alpha()
        self.image = pygame.transform.smoothscale(
            self.raw_image, (self.width, self.height))
        self.position = position
        self.rotate_state = 0

    def flip(self):
        if self.visible == False:
            self.visible = True
            self.raw_image = pygame.image.load(
                self.__picture).convert_alpha()
        else:
            self.visible = False
            self.raw_image = pygame.image.load(
                self.back_picture).convert_alpha()
        self.image = pygame.transform.smoothscale(
            self.raw_image, (self.width, self.height))
        self.rotate(random.randint(0, 3) * 90)

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)
        angle = angle // 90
        self.rotate_state += angle
        self.rotate_state %= 2
        if self.rotate_state == 0:
            self.gates = [1, 1, 0, 0]
        elif self.rotate_state == 1:
            self.gates = [0, 0, 1, 1]

    def in_utility(self, player):
        super().in_utility(player)
        player.move_times += 1
