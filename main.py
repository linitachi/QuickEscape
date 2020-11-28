import sys
import time
import random

import pygame
# from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT, USEREVENT
from pygame.locals import *
from map import Map


WHITE = (255, 255, 255)
number_of_players = 2
FPS = 60
turn_over = USEREVENT+1


def main():
    M = Map()
    turn = 9
    my_font = pygame.font.SysFont(None, 30)

    imgPos = pygame.Rect((350, 200), (0, 0))
    i = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEMOTION:
                if event.buttons[2] == 1:
                    rel = event.rel
                    imgPos.x += rel[0]
                    imgPos.y += rel[1]
            if event.type == MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if event.button == 1:
                    for k in range(25):
                        if M.map_list[k].rect.collidepoint(mouse_position):
                            M.map_list[k].flip()
                        if k < 4:
                            try:
                                __index = M.number_of_players[i].map_list_position.index(
                                    1)
                                if M.move_button[k].collidepoint(mouse_position):
                                    try:
                                        if k == 0:
                                            __index -= 5
                                            next = 1
                                        elif k == 1:
                                            __index += 5
                                            next = 0
                                        elif k == 2:
                                            __index -= 1
                                            next = 3
                                        elif k == 3:
                                            __index += 1
                                            next = 2
                                        if M.map_list[__index].visible == False:
                                            M.map_list[__index].flip()
                                        if M.map_list[__index].gates[next] == 1 and M.number_of_players[i].move(k):
                                            print("我走囉")
                                    except:
                                        pass

                            except:
                                pass
                                # pygame.event.post(pygame.event.Event(turn_over))
            if event.type == turn_over:
                turn -= 1
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
        M.print_move_icon(M.number_of_players[i], imgPos)
        for player in range(number_of_players):
            M.print_player(imgPos, player)

        # M.window_surface.blit(M.player.image, imgPos)
        # M.window_surface.blit(
        #     M.player2.image, (imgPos[0] + 75, imgPos[1]))
        turn_text = my_font.render(
            'Turn of:{} Turn:{}'.format(M.number_of_players[i].id, turn), True, (255, 255, 255))
        M.window_surface.blit(turn_text, (10, 0))
        pygame.display.flip()


if __name__ == '__main__':
    main()
