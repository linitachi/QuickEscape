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
game_over = USEREVENT+2


def main():
    win_message = ""
    M = Map(number_of_players)
    turn = 9
    __rotate = False
    my_font = pygame.font.SysFont(None, 30)

    imgPos = pygame.Rect((350, 200), (0, 0))
    i = 0
    __tem_rotate_state = []
    while True:
        if turn > 0:
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
                        if M.stay_icon_rect.collidepoint(mouse_position):
                            pygame.event.post(
                                pygame.event.Event(turn_over))
                        # Click rotate_icon
                        if M.rotate_icon_rect.collidepoint(mouse_position):
                            __rotate = False
                            __tem = 0
                            __origin_times = M.number_of_players[i].rotate_times
                            for k in range(25):
                                if __tem_rotate_state[k] != M.map_list[k].rotate_state:
                                    M.number_of_players[i].rotate_room()
                                    __tem += 1
                            # 檢查是否超過旋轉次數
                            if M.number_of_players[i].rotate_times < 0:
                                if __tem > 2 and __origin_times == 2:
                                    M.number_of_players[i].init_rotate_times()
                                elif __tem > 2 and __origin_times == 1:
                                    M.number_of_players[i].rotate_times = 1
                                else:
                                    M.number_of_players[i].rotate_times = 0
                                for k in range(25):
                                    M.map_list[k].reset_room(
                                        __tem_rotate_state[k])
                            __tem_rotate_state = []
                        for k in range(25):
                            # 已翻開的房間才可以旋轉 旋轉前先暫存狀態 以一開始的狀態為主
                            if len(__tem_rotate_state) < 25:
                                __tem_rotate_state.append(
                                    M.map_list[k].rotate_state)
                            if M.map_list[k].rect.collidepoint(mouse_position) and M.map_list[k].visible:
                                M.map_list[k].rotate(90)
                                __rotate = True
                            if k < 4:
                                if __rotate == False:
                                    try:
                                        # 尋找player的房間index
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
                                                    pygame.event.post(
                                                        pygame.event.Event(turn_over))
                                                if M.map_list[__index].gates[next] == 1 and M.number_of_players[i].move(k):
                                                    if not pygame.event.peek(turn_over):
                                                        pygame.event.post(
                                                            pygame.event.Event(turn_over))
                                            except:
                                                pass
                                    except:
                                        pass
                if event.type == turn_over:
                    i += 1
                    __tem_rotate_state = []
                    __rotate = False
                    if i == number_of_players:
                        turn -= 1
                        # 檢查是否有人在出口
                        for i in range(number_of_players):
                            M.number_of_players[i].init_rotate_times()
                            if M.escape_index == M.number_of_players[i].map_list_position.index(1):
                                M.map_list[M.escape_index].reduce_save_player(
                                    M.number_of_players[i].id)
                            else:
                                M.map_list[M.escape_index].init_save_player(
                                    M.number_of_players[i])
                        i = 0

                    __player_win = list(
                        M.map_list[M.escape_index].save_player.values())
                    for k in range(len(__player_win)):
                        if __player_win[k] == 0:
                            win_message += "player%s" % k + "  "
                            turn = 0
                    if turn == 0:
                        win_message += "win"

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
                M.print_stay()
                # 確定旋轉完才能行走
                if __rotate:
                    M.print_rotate()
                else:
                    M.print_move_icon(M.number_of_players[i], imgPos)

                for player in range(number_of_players):
                    M.print_player(imgPos, player)

                turn_text = my_font.render(
                    'Turn of:{} Turn:{} Rotate_Time:{}'.format(M.number_of_players[i].id, turn, M.number_of_players[i].rotate_times), True, (255, 255, 255))
                M.window_surface.blit(turn_text, (10, 0))
                pygame.display.flip()
        else:
            pygame.init()
            M.window_surface.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if win_message == "win":
                win_message = "NoBody Runaway !!"
            turn_text = my_font.render(
                win_message, True, (255, 255, 255))
            M.window_surface.blit(turn_text, (50, 50))
            pygame.display.flip()


if __name__ == '__main__':
    main()
