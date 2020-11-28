from room import Room
import pygame


class RoomtypeA(Room):
    def __init__(self, position=(150, 150), width=250, height=250):
        super().__init__(position, width, height)
        self.gates = [1, 1, 1, 0]
        self.__picture = "picture\\roomA.jpg"
        self.raw_image = pygame.image.load(self.back_picture).convert_alpha()
        self.image = pygame.transform.scale(
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
        self.image = pygame.transform.scale(
            self.raw_image, (self.width, self.height))
