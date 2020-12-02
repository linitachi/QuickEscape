import pygame
from pygame.locals import *
import sys
add_icon_size = 100
finished = USEREVENT+1


class Menu:
    def __init__(self):
        pygame.init()
        WINDOW_WIDTH = 1000
        WINDOW_HEIGHT = 700
        BLACK = (0, 0, 0)
        self.window_surface = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption('Welcome to QuickEscape!!')

        self.window_surface.fill(BLACK)
        self.init_button()
        self.number = self.main()

    def init_button(self):
        __picture = "picture\\menu\\add.png"
        __raw_image = pygame.image.load(__picture).convert_alpha()
        self.add_icon = pygame.transform.smoothscale(
            __raw_image, (add_icon_size, add_icon_size))
        self.add_icon_rect = self.add_icon.get_rect()

        __picture = "picture\\menu\\reduce.png"
        __raw_image = pygame.image.load(__picture).convert_alpha()
        self.reduce_icon = pygame.transform.smoothscale(
            __raw_image, (add_icon_size, add_icon_size))
        self.reduce_icon_rect = self.add_icon.get_rect()

        __picture = "picture\\menu\\startgame.png"
        __raw_image = pygame.image.load(__picture).convert_alpha()
        self.start_icon = pygame.transform.smoothscale(
            __raw_image, (600, 250))
        self.start_icon_rect = self.start_icon.get_rect()

        __picture = "picture\\menu\\playagain.png"
        __raw_image = pygame.image.load(__picture).convert_alpha()
        self.playagain_icon = pygame.transform.smoothscale(
            __raw_image, (600, 250))
        self.playagain_icon_rect = self.playagain_icon.get_rect()

        __picture = "picture\\menu\\text.png"
        __raw_image = pygame.image.load(__picture).convert_alpha()
        self.text = pygame.transform.smoothscale(
            __raw_image, (800, 200))

    def print_button(self):
        x, y = self.window_surface.get_size()
        self.window_surface.blit(
            self.add_icon, (x - 150, y/3-add_icon_size/2))
        self.add_icon_rect.topleft = (x - 150, y/3-add_icon_size/2)

        self.window_surface.blit(
            self.reduce_icon, (50, y/3-add_icon_size/3))
        self.reduce_icon_rect.topleft = (50, y/3-add_icon_size/2)

        self.window_surface.blit(
            self.start_icon, (x/10*2, y/7*4))
        self.start_icon_rect.topleft = (x / 10 * 2, y / 7 * 4)

        self.window_surface.blit(
            self.text, (x/20*2, 0))

    def print_end(self):
        x, y = self.window_surface.get_size()
        self.window_surface.blit(
            self.playagain_icon, (x/10*2, y / 7 * 4))
        self.playagain_icon_rect.topleft = (x / 10 * 2, y / 7 * 4)

    def main(self):
        my_font = pygame.font.SysFont(None, 200)
        number = 2
        while True:
            for event in pygame.event.get():
                if event.type == finished:
                    self.window_surface.fill((0, 0, 0))
                    turn_text = my_font.render(
                        "GAME START!!", True, (255, 255, 255))
                    self.window_surface.blit(turn_text, (50, 175))
                    pygame.display.flip()
                    return number
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    if event.button == 1:
                        if self.add_icon_rect.collidepoint(mouse_position):
                            number += 1
                            if number > 5:
                                number = 6
                        elif self.reduce_icon_rect.collidepoint(mouse_position):
                            number -= 1
                            if number < 2:
                                number = 1

                        elif self.start_icon_rect.collidepoint(mouse_position):
                            pygame.event.post(
                                pygame.event.Event(finished))

            self.window_surface.fill((0, 0, 0))
            turn_text = my_font.render(
                str(number), True, (255, 255, 255))
            self.window_surface.blit(turn_text, (450, 175))
            self.print_button()
            pygame.display.flip()

    def end_menu(self, win_message):
        my_font = pygame.font.SysFont(None, 50)
        self.window_surface.fill((0, 0, 0))
        if win_message == "WIN!!":
            win_message = "NoBody Runaway !!"
            pygame.display.set_caption('NoBody Runaway !!')
        else:
            win_message = win_message.split(" ")
            pygame.display.set_caption('Happy end!!')
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    if event.button == 1:
                        if self.playagain_icon_rect.collidepoint(mouse_position):
                            return
            for i in range(len(win_message)):
                turn_text = my_font.render(
                    win_message[i], True, (255, 255, 255))
                self.window_surface.blit(turn_text, (425, 50+50*i))
            self.print_end()
            pygame.display.flip()
