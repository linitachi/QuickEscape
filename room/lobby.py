from room import Room
import pygame


class Lobby(Room):
    def __init__(self, position=(150, 150), width=250, height=250):
        super().__init__(position, width, height)
        self.gates = [1, 1, 1, 1]
        __picture = "picture\lobby.jpg"
        self.raw_image = pygame.image.load(__picture).convert_alpha()
        self.image = pygame.transform.scale(self.raw_image, (width, height))
        self.position = position
