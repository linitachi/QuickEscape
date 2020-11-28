import sys
import time
import random

import pygame
# from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT, USEREVENT
from pygame.locals import *
from map import Map


WHITE = (255, 255, 255)
IMAGEWIDTH = 300
IMAGEHEIGHT = 200
FPS = 60


def main():
    M = Map()
    turn = 9
    my_font = pygame.font.SysFont(None, 30)

    imgPos = pygame.Rect(M.lobby.position, (0, 0))
    i = 10
    turn_text = my_font.render(
        'Turn of:{} Turn:{}'.format(M.people.id, turn), True, (255, 255, 255))
    while True:
        # 迭代整個事件迴圈，若有符合事件則對應處理
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEMOTION:
                if event.buttons[0] == 1:
                    rel = event.rel
                    imgPos.x += rel[0]
                    imgPos.y += rel[1]

            # TODO:zoom功能

            # if event.type == MOUSEWHEEL:
            #     if event.y == 1:
            #         M.lobby.image = M.lobby.zoom(M.lobby.raw_image,
            #                                      i, i, 1)
            #     if event.y == -1:
            #         M.lobby.image = M.lobby.zoom(M.lobby.raw_image,
            #                                      i, i, 0)
        M.window_surface.fill(0)

        M.print_map(imgPos)

        M.window_surface.blit(M.people.image, imgPos)
        M.window_surface.blit(
            M.people2.image, (imgPos[0] + 50, imgPos[1]))

        M.window_surface.blit(turn_text, (10, 0))
        pygame.display.flip()


if __name__ == '__main__':
    main()
