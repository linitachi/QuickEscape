import pygame


class Player():
    def __init__(self, picture, position=(150, 150), width=250, height=250, id=""):
        self.raw_image = pygame.image.load(picture).convert_alpha()
        self.image = pygame.transform.scale(self.raw_image, (width, height))
        self.position = position
        self.id = id
        self.map_list_position = [0] * 25
        self.map_list_position[12] = 1
