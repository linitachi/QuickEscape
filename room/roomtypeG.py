from room import Room
import pygame
import random

# 交換房間:擁有四個路口的房間，當玩家進入後，與大廳以外的隨機一個房間交換，如果未翻開則翻開該房間，並執行交換後的房間進入效果


class RoomtypeG(Room):
    def __init__(self, position=(150, 150), width=250, height=250):
        super().__init__(position, width, height)
        self.gates = [1, 1, 1, 1]
        self.__picture = "picture\\roomG.png"
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
        __tem = random.randint(0, 25)
        return "Random_change"

    def change_room(self):
        __tem = random.randint(0, 24)
        while __tem == 12:
            __tem = random.randint(0, 24)
        return __tem
