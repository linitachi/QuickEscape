import pygame


class Room:
    def __init__(self, position=(150, 150), width=250, height=250):
        # 代表房間的出口 1為可以走 0為不可走
        # 上下左右
        self.gates = [0, 0, 0, 0]
        self.width = width
        self.height = height
        self.numofchars = [0, 0, 0, 0, 0, 0]
        self.visible = False
        self.back_picture = "picture\\back.jpg"
        self.raw_image = pygame.image.load(self.back_picture).convert_alpha()
        self.image = pygame.transform.scale(
            self.raw_image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (position[0], position[1])
        self.rotate_state = 0

    def zoom(self, raw_image, width, height, isbig):
        if isbig:
            self.height += height
            self.width += width
        else:
            self.height -= height
            self.width -= width
        return pygame.transform.scale(raw_image, (self.width, self.height))

    def flip(self):
        pass

    def get_visible(self):
        return self.visible

    def rotate(self, angle):
        pass
