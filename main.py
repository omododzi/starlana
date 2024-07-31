import os
import pygame
import random

pygame.init()
zvezdolet = pygame.image.load(r'C:\Users\User\PycharmProjects\pythonProject2\zvezdolet.png')
zvezdolet = pygame.transform.scale(zvezdolet, (80, 80))
laser = pygame.image.load(r'C:\Users\User\Downloads\laser.png')
laser = pygame.transform.scale(laser, (20, 40))
bg = pygame.image.load(r'C:\Users\User\PycharmProjects\pythonProject2\cosmos.png')
bg = pygame.transform.scale(bg, (700, 950))
# Размер окна------------------------------
WIDTH = 700
HEIGHT = 950
FPS = 45

# Создание окна---------------------
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("звездостранец")
clock = pygame.time.Clock()
screen.fill("black")
#-------------------------------------------------
speed = 9
moving_left = False
moving_right = False
moving_up = False
moving_down = False
rotat_l = False
rotat_r = False
meteors = []
speed_mete = 3
# Цвета-------------------------------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
#рект самолета_----------------------------
zvezdolet_rect = zvezdolet.get_rect()
zvezdolet_rect.x = 300
zvezdolet_rect.y = 850

angle = 0


#----------------------------------------------------

def falling_meteors(meteors, screen_width):

    if len(meteors) < 3:
        meteor_size_min = 50
        meteor_size_max = 100
        screen_width = 700
        x_mete = random.randint(90, 620)
        y_mete = 0
        mete = pygame.image.load('mete-no-bg-preview (carve.photos).png')
        size = random.randint(meteor_size_min, meteor_size_max)
        mete = pygame.transform.scale(mete, (size, size))
        falling = mete
        mete_rect = mete.get_rect()
        mete_rect.x = x_mete
        mete_rect.y = y_mete
        meteors.append((mete_rect, falling))
#-----------------------------------------------------------------
laser_rect = laser.get_rect()
hu = 0
uh = 0
score = pygame.font.SysFont("сбито",50)
score_2 = pygame.font.SysFont("упущено",50)


a = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # передвижение ---------------------------------------------------------
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            elif event.key == pygame.K_d:
                moving_right = True
            elif event.key == pygame.K_w:
                moving_up = True
            elif event.key == pygame.K_s:
                moving_down = True
            elif event.key == pygame.K_q:
                rotat_l = True
                angle += 1
            elif event.key == pygame.K_e:
                rotat_r = True
                angle -= 1

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            elif event.key == pygame.K_d:
                moving_right = False
            elif event.key == pygame.K_w:
                moving_up = False
            elif event.key == pygame.K_s:
                moving_down = False
            elif event.key == pygame.K_q:
                rotat_l = False
            elif event.key == pygame.K_e:
                rotat_r = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and a == False:
                a = True
                laser_rect.x = zvezdolet_rect.x + 40
                laser_rect.y = zvezdolet_rect.y





    screen.blit(bg,(0,0))
    #щетчик----------------------------------------
    destrou = score.render(str(hu),0,(WHITE))
    not_destrou = score.render(str(uh), 0, (WHITE))
    screen.blit(destrou,(50,50))
    screen.blit(not_destrou, (WIDTH - 50, 50))
    # лазер------------------------------------------------------
    if a ==True:
        screen.blit(laser, laser_rect)
        laser_rect.y -= 10

    # звездолет-----------------------------------------------------------
    centr = (zvezdolet_rect.x+40,zvezdolet_rect.y+40)
    if moving_left and zvezdolet_rect.x >= 0:
        zvezdolet_rect.x -= speed
    if moving_right and zvezdolet_rect.x <= 620:
        zvezdolet_rect.x += speed
    if moving_up and zvezdolet_rect.y >= 0:
        zvezdolet_rect.y -= speed
    if moving_down and zvezdolet_rect.y <= 880:
        zvezdolet_rect.y += speed
    if rotat_l == True:
        centr = pygame.transform.rotate(zvezdolet, 10)
    if rotat_r == True:
        centr = pygame.transform.rotate(zvezdolet, 10)
    screen.blit(zvezdolet, zvezdolet_rect)
    # ---------------------------------------------------------------------------------
    # генерация метеоров--------------------------------------------------------------
    falling_meteors(meteors, WIDTH)

    for i in meteors:
        mete_rect = i[0]
        mete_rect.y += speed_mete
        falling = i[1]
        screen.blit(falling, mete_rect)

        if zvezdolet_rect.colliderect(mete_rect):
            running = False
        if mete_rect.y >= 950:
            meteors.remove(i)
            speed_mete += 0.5
            uh+=1

        if laser_rect.colliderect(mete_rect):
            a = False
            laser_rect.y = -1000
            meteors.remove(i)
            hu+=1
        if laser_rect.y <= 0:
            a = False
            laser_rect.y = -1000

    clock.tick(FPS)
    pygame.display.update()