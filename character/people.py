import pygame


class Player():
    def __init__(self, picture, position=(150, 150), width=250, height=250, id=""):
        self.raw_image = pygame.image.load(picture).convert_alpha()
        self.image = pygame.transform.smoothscale(
            self.raw_image, (width, height))
        self.position = position
        self.id = id
        self.map_list_position = 12
        self.rotate_times = 2
        self.move_times = 2
        self.Live = "LIVE"

    def move(self, direction):
        # 上0 下1 左2 右3
        __index = self.map_list_position
        # 往上
        if direction == 0:
            self.map_list_position = __index - 5
            return True
        # 往下
        elif direction == 1:
            self.map_list_position = __index + 5
            return True
        # 往左
        elif direction == 2:
            self.map_list_position = __index - 1
            return True
        # 往右
        elif direction == 3:
            self.map_list_position = __index + 1
            return True
        return False

    def rotate_room(self):
        self.rotate_times -= 1

    def init_rotate_times(self, num):
        self.rotate_times = num

    def init_move_times(self, num):
        self.move_times = num

    def reduce_move_times(self):
        self.move_times -= 1
