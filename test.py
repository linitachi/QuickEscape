
import pygame
import sys
from pygame.locals import *
import myclass

pygame.init()
screen_size = width, height = 480, 700
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('飞机大战')
bg = pygame.image.load('./images/background.png').convert()

pygame.mixer.music.load('./sound/game_music.ogg')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)


def add_big_enemies(group1, group2, num):
    for big_enemy_num in range(num):
        each_big_enemy = myclass.BigEnemy(screen_size)
        group1.add(each_big_enemy)
        group2.add(each_big_enemy)


def add_mid_enemies(group1, group2, num):
    for mid_enemy_num in range(num):
        each_mid_enemy = myclass.MidEnemy(screen_size)
        group1.add(each_mid_enemy)
        group2.add(each_mid_enemy)


def add_small_enemies(group1, group2, num):
    for small_enemy_num in range(num):
        each_small_enemy = myclass.SmallEnemy(screen_size)
        group1.add(each_small_enemy)
        group2.add(each_small_enemy)


def main():
    clock = pygame.time.Clock()

    heroPlane = myclass.myPlane(screen, screen_size)

    enemies = pygame.sprite.Group()

    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies, enemies, 2)

    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies, enemies, 4)

    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies, enemies, 15)

    bullet1 = []
    bullet1_index = 0
    BULLET1_NUM = 5
    for i in range(BULLET1_NUM):
        bullet1.append(myclass.Bullet(heroPlane.rect.midtop, True))

    small_destroy_index = 0
    mid_destroy_index = 0
    big_destroy_index = 0
    hero_destroy_index = 0

    life_image = pygame.image.load("images/life.png").convert_alpha()
    life_rect = life_image.get_rect()
    life_NUM = 3

    score = 0
    score_font = pygame.font.Font("font/font.ttf", 30)
    WhiteFont = (255, 255, 255)
    gameover_font = pygame.font.Font("font/font.ttf", 48)
    again_image = pygame.image.load("images/again.png").convert_alpha()
    gameover_image = pygame.image.load("images/gameover.png").convert_alpha()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_UP]:
            heroPlane.moveUp()
        if key_pressed[K_DOWN]:
            heroPlane.moveDown()
        if key_pressed[K_LEFT]:
            heroPlane.moveLeft()
        if key_pressed[K_RIGHT]:
            heroPlane.moveRight()

        screen.blit(bg, (0, 0))
        heroPlane.time_delay()

        if life_NUM > 0:
            for each in big_enemies:
                if each.active == True:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:
                    if not (heroPlane.delay % 3):
                        screen.blit(
                            each.destroy_images[big_destroy_index], each.rect)
                        big_destroy_index = (big_destroy_index + 1) % 6
                        if big_destroy_index == 0:
                            each.play_sound()
                            score += 300
                            each.reset()

            for each in mid_enemies:
                if each.active == True:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:
                    if not (heroPlane.delay % 3):
                        screen.blit(
                            each.destroy_images[mid_destroy_index], each.rect)
                        mid_destroy_index = (mid_destroy_index + 1) % 4
                        if mid_destroy_index == 0:
                            each.play_sound()
                            score += 200
                            each.reset()

            for each in small_enemies:
                if each.active == True:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:
                    if not (heroPlane.delay % 3):
                        screen.blit(
                            each.destroy_images[small_destroy_index], each.rect)
                        small_destroy_index = (small_destroy_index + 1) % 4
                        if small_destroy_index == 0:
                            each.play_sound()
                            score += 100
                            each.reset()

            if heroPlane.active == True:
                heroPlane.animation()
            else:
                if not (heroPlane.delay % 3):
                    screen.blit(
                        heroPlane.destroy_images[hero_destroy_index], heroPlane.rect)
                    hero_destroy_index = (hero_destroy_index + 1) % 4
                    if hero_destroy_index == 0:
                        life_NUM -= 1
                        heroPlane.play_sound()
                        heroPlane.reset()

            if life_NUM > 0:
                for i in range(life_NUM):
                    screen.blit(life_image, (width - 10 - (i + 1) *
                                             life_rect.width, height - 10 - life_rect.height))

            if not (heroPlane.delay % 10):
                bullet1[bullet1_index].reset(heroPlane.rect.midtop)
                bullet1_index = (bullet1_index + 1) % BULLET1_NUM

            for each in bullet1:
                if each.active == True:
                    each.move()
                    screen.blit(each.image, each.rect)
                    enemies_hit = pygame.sprite.spritecollide(
                        each, enemies, False, pygame.sprite.collide_mask)
                    if enemies_hit:
                        each.active = False
                        for e in enemies_hit:
                            if e in mid_enemies or e in big_enemies:
                                e.energy -= 1
                                if e.energy == 0:
                                    e.active = False
                            else:
                                e.active = False
                else:
                    each.reset(heroPlane.rect.midtop)

            enemies_collided = pygame.sprite.spritecollide(
                heroPlane, enemies, False, pygame.sprite.collide_mask)

            if enemies_collided:
                heroPlane.active = False
                for each in enemies_collided:
                    each.active = False

            score_surface = score_font.render(
                "Score : %s" % str(score), True, WhiteFont)
            screen.blit(score_surface, (10, 5))
        else:
            pygame.mixer.music.stop()

            gameover_score = gameover_font.render(
                "Score : %s" % str(score), True, WhiteFont)
            screen.blit(gameover_score, (100, 200))
            screen.blit(again_image, (90, 350))
            screen.blit(gameover_image, (90, 450))

            mouse_down = pygame.mouse.get_pressed()
            if mouse_down[0]:
                pos = pygame.mouse.get_pos()
                if 90 < pos[0] < 390 and 350 < pos[1] < 390:
                    main()
                elif 90 < pos[0] < 390 and 450 < pos[1] < 490:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
