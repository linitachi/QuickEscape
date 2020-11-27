import pygame


class People():
    def __init__(self, picture, position=(150, 150), width=250, height=250, id=""):
        self.raw_image = pygame.image.load(picture).convert_alpha()
        self.image = pygame.transform.scale(self.raw_image, (width, height))
        self.position = position
        self.id = id
