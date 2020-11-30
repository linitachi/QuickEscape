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
        self.image = pygame.transform.smoothscale(
            self.raw_image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (position[0], position[1])
        self.rotate_state = -1

    def zoom(self, raw_image, width, height, isbig):
        if isbig:
            self.height += height
            self.width += width
        else:
            self.height -= height
            self.width -= width
        return pygame.transform.smoothscale(raw_image, (self.width, self.height))

    def flip(self):
        pass

    def get_visible(self):
        return self.visible

    def rotate(self, angle):
        pass

    def reset_room(self, origin_state):
        __angle = (origin_state - self.rotate_state) * 90
        if origin_state - self.rotate_state == 3:
            __angle = -90
        elif origin_state - self.rotate_state == -3:
            __angle = 90
        self.rotate(__angle)

    # 待在房間的效果
    def utility(self, player):
        if player.Live == "DYING":
            player.Live = "LIVE"

    # 離開房間的效果
    def move_utility(self, player):
        print("走出去")

        pass

    # 進去房間的效果
    def in_utility(self, player):
        print("哈哈")
        if player.Live == "DYING":
            player.Live = "LIVE"
