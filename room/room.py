import pygame


class Room:
    def __init__(self, position=(150, 150), width=250, height=250):
        # 代表房間的出口 1為可以走 0為不可走
        self.gates = [0, 0, 0, 0]
        self.width = width
        self.height = height
        self.numofchars = [0, 0, 0, 0, 0, 0]

    def zoom(self, raw_image, width, height, isbig):
        if isbig:
            self.height += height
            self.width += width
        else:
            self.height -= height
            self.width -= width
        return pygame.transform.scale(raw_image, (self.width, self.height))
