import sys
import time
import random

import pygame
# from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT, USEREVENT
from pygame.locals import *
from map import Map
from menu import Menu

WHITE = (255, 255, 255)
FPS = 60
turn_over = USEREVENT+1
game_over = USEREVENT + 2


def main(number_of_players=2):
    if number_of_players < 4:
        turn = 12
    else:
        turn = 9
    player_index = [i for i in range(number_of_players)]
    win_message = ""
    M = Map(number_of_players)
    __rotate = False
    __dice_confirm = True
    __dice = True
    __move = False
    my_font = pygame.font.SysFont(None, 50)

    imgPos = pygame.Rect((350, 200), (0, 0))
    i = 0
    player_turn = random.sample(player_index, len(player_index))
    __tem_rotate_state = []
    __move_times, __rotate_times = M.get_all_dice()
    M.player_list[player_turn[i]].init_rotate_times(__rotate_times)
    M.player_list[player_turn[i]].init_move_times(__move_times)

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
                        # 限制使用者移動螢幕的範圍
                        if imgPos.x > 760:
                            imgPos.x = 760
                        if imgPos.x < 72:
                            imgPos.x = 72
                        if imgPos.y > 734:
                            imgPos.y = 734
                        if imgPos.y < -225:
                            imgPos.y = -225

                if event.type == MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    if event.button == 1:
                        # 點擊個別的骰子來重骰
                        __all_dice_down = 0
                        for k in M.dice_list:
                            if k.roll_times > 0 and k.dice_icon_rect.collidepoint(mouse_position) and __dice == True:
                                print("骰子", k.test)
                                k.roll_dice()
                                __move_times, __rotate_times = M.get_all_dice()
                                M.player_list[player_turn[i]].init_rotate_times(
                                    __rotate_times)
                                M.player_list[player_turn[i]
                                              ].init_move_times(__move_times)
                            __all_dice_down += k.roll_times
                        if __all_dice_down == 0:
                            __dice_confirm = False
                            __move = True

                        if __dice_confirm == True and M.dice_confirm_rect.collidepoint(mouse_position):
                            __dice_confirm = False
                            __dice = False
                            __move = True

                            __move_times, __rotate_times = M.get_all_dice()
                            M.player_list[player_turn[i]].init_rotate_times(
                                __rotate_times)
                            M.player_list[player_turn[i]
                                          ].init_move_times(__move_times)
                            break
                        if M.stay_icon_rect.collidepoint(mouse_position):
                            print("stay")
                            pygame.event.post(
                                pygame.event.Event(turn_over))
                            break

                        # Click rotate_icon
                        if M.rotate_icon_rect.collidepoint(mouse_position) and __rotate == True:
                            __rotate = False
                            __tem = 0
                            __origin_times = M.player_list[player_turn[i]
                                                           ].rotate_times
                            for k in range(25):
                                if __tem_rotate_state[k] != M.map_list[k].rotate_state:
                                    M.player_list[player_turn[i]].rotate_room()
                                    __tem += 1
                            # 檢查是否超過旋轉次數 超過的話就重置旋轉次數與房間
                            if M.player_list[player_turn[i]].rotate_times < 0:
                                if __tem > 2 and __origin_times > 0:
                                    M.player_list[player_turn[i]
                                                  ].rotate_times = __origin_times
                                else:
                                    M.player_list[player_turn[i]
                                                  ].rotate_times = 0
                                for k in range(25):
                                    M.map_list[k].reset_room(
                                        __tem_rotate_state[k])
                            __tem_rotate_state = []
                            break

                        for k in range(25):
                            # 已翻開的房間才可以旋轉 旋轉前先暫存狀態 以一開始的狀態為主
                            if len(__tem_rotate_state) < 25:
                                __tem_rotate_state.append(
                                    M.map_list[k].rotate_state)
                            if M.map_list[k].rect.collidepoint(mouse_position) and M.map_list[k].visible and M.map_list[k].rotate_state != -1 and __dice_confirm == False:
                                M.map_list[k].rotate(90)
                                __rotate = True
                        # 移動的button
                        for k in range(4):
                            if __rotate == False and __move == True:
                                    # 尋找player的房間index
                                __cur_index = M.player_list[player_turn[i]
                                                            ].map_list_position
                                if M.move_button[k] != 0 and M.move_button[k].collidepoint(mouse_position) and M.player_list[player_turn[i]].move_times > 0:
                                    __new_index, next = M.player_move_criteria(
                                        k, __cur_index)
                                    # 代表是可能可以移動的
                                    if __new_index != -1:
                                        if M.map_list[__new_index].visible == False:
                                            M.map_list[__new_index].flip()
                                            # 當翻開房間後，把所有房間狀態記錄起來
                                            __tem_rotate_state = []
                                            for w in range(25):
                                                __tem_rotate_state.append(
                                                    M.map_list[w].rotate_state)
                                            if M.map_list[__new_index].gates[next] != 1:
                                                M.player_list[player_turn[i]].reduce_move_times(
                                                )

                                        if M.map_list[__new_index].gates[next] == 1 and M.player_list[player_turn[i]].move(k):
                                            M.map_list[__new_index].in_utility(
                                                M.player_list[player_turn[i]])
                                            M.map_list[__cur_index].move_utility(
                                                M.player_list[player_turn[i]])
                                            M.player_list[player_turn[i]].reduce_move_times(
                                            )

                if M.player_list[player_turn[i]].rotate_times == 0 and M.player_list[player_turn[i]].move_times == 0:
                    M.player_list[player_turn[i]].rotate_times = -1
                    if not pygame.event.peek(turn_over):
                        pygame.event.post(pygame.event.Event(turn_over))

                if event.type == turn_over:
                    M.map_list[M.player_list[player_turn[i]].map_list_position].utility(
                        M.player_list[player_turn[i]])

                    #  把死掉的玩家移出遊戲
                    print(M.player_list[player_turn[i]].id,
                          M.player_list[player_turn[i]].Live)
                    if M.player_list[player_turn[i]].Live == "DIED":
                        print(player_turn[i], "已經死掉了")
                        player_index.pop(player_index.index(player_turn[i]))
                    i += 1
                    for k in M.dice_list:
                        k.init_dice()
                    __move_times, __rotate_times = M.get_all_dice()

                    __tem_rotate_state = []
                    __rotate = False
                    __dice_confirm = True
                    __dice = True
                    __move = False

                    if i == len(player_turn):
                        turn -= 1
                        # 檢查是否有人在出口
                        for i in range(len(player_turn)):
                            M.player_list[player_turn[i]].init_rotate_times(
                                __rotate_times)
                            M.player_list[player_turn[i]
                                          ].init_move_times(__move_times)
                            if M.escape_index == M.player_list[player_turn[i]].map_list_position:
                                M.map_list[M.escape_index].reduce_save_player(
                                    M.player_list[player_turn[i]].id)
                            else:
                                M.map_list[M.escape_index].init_save_player(
                                    M.player_list[player_turn[i]])

                        i = 0
                        player_turn = random.sample(
                            player_index, len(player_index))
                        print("下回合人數", len(player_turn))
                        # 如果下回合沒有玩家可以行動(代表玩家都死光了)
                        if len(player_turn) == 0:
                            turn = 0
                            win_message += "win"
                            break
                    else:
                        M.player_list[player_turn[i]].init_rotate_times(
                            __rotate_times)
                        M.player_list[player_turn[i]
                                      ].init_move_times(__move_times)

                    # 畫面自動移動到腳色位置
                    imgPos[0] = 350+imgPos[0] - M.map_list[M.player_list[player_turn[i]
                                                                         ].map_list_position].rect.topleft[0]
                    imgPos[1] = 200+imgPos[1]-M.map_list[M.player_list[player_turn[i]
                                                                       ].map_list_position].rect.topleft[1]
                    print(imgPos, M.map_list[M.player_list[player_turn[i]
                                                           ].map_list_position].rect.topleft)
                    # 檢查是否有玩家獲勝
                    __player_win = list(
                        M.map_list[M.escape_index].save_player.values())
                    for k in range(len(__player_win)):
                        if __player_win[k] == 0:
                            win_message += "%s" % M.player_list[player_turn[i]].id + "  "
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
                # 確定旋轉完才能行走
                if __rotate:
                    M.print_rotate()
                elif M.player_list[player_turn[i]].move_times > 0 and __move == True:
                    M.print_move_icon(M.player_list[player_turn[i]], imgPos)

                for player in player_index:
                    M.print_player(imgPos, player)

                M.print_stay()
                M.print_dice()
                if __dice_confirm:
                    M.print_dice_confirm()
                turn_text = my_font.render(
                    'Turn of:{} Turn:{} Move:{} Rotate:{}'.format(M.player_list[player_turn[i]].id, turn, M.player_list[player_turn[i]].move_times, M.player_list[player_turn[i]].rotate_times), True, (255, 255, 255))
                M.window_surface.blit(turn_text, (0, 0))
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
            M.window_surface.blit(turn_text, (425, 400))
            pygame.display.flip()


if __name__ == '__main__':
    m = Menu()
    main(m.number)
