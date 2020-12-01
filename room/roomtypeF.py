from room import Room
import pygame
import random

# 重力房間:擁有四個路口的房間，當玩家進入後，使玩家移動次數-1
# 超重力房間: 擁有四個路口的房間，當玩家進入後，使玩家移動次數歸零


class RoomtypeF(Room):
    def __init__(self, position=(150, 150), width=250, height=250):
        super().__init__(position, width, height)
        self.gates = [1, 1, 1, 1]
        self.__tem = random.randint(0, 5)
        if self.__tem == 0:
            self.__picture = "picture\\roomF2.png"
        else:
            self.__picture = "picture\\roomF.png"
        self.raw_image = pygame.image.load(self.back_picture).convert_alpha()
        self.image = pygame.transform.smoothscale(
            self.raw_image, (self.width, self.height))
        self.position = position

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

    def in_utility(self, player):
        super().in_utility(player)
        if player.move_times > 0 and self.__tem != 0:
            player.move_times -= 1
        else:
            player.move_times = 0
