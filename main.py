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
    imgPos = pygame.Rect(M.lobby.position, (0, 0))
    i = 10
    while True:
        # 迭代整個事件迴圈，若有符合事件則對應處理
        for event in pygame.event.get():
            # 當使用者結束視窗，程式也結束
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEMOTION:
                if event.buttons[0] == 1:
                    # clicked and moving
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
        M.window_surface.blit(M.lobby.image, imgPos)
        M.window_surface.blit(
            M.roomtypeA.image, (imgPos[0]-300, imgPos[1]-0))

        pygame.display.flip()


if __name__ == '__main__':
    main()
