import pygame
import winsound
import random

pygame.init()
size = (800,600)
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
running = True
position_x_ball = 0
position_Y_ball = 300
soma = pygame.image.load("AriaSoma_Sprite.png")
background = pygame.image.load("castle.png")
pygame.display.set_caption("Castlevania Rise of Sorrow")
pygame.display.set_icon(soma)
speed = 1
position_x_red_ball = 400
movement_red_ball_x = 0
movement_red_ball_y = 0
position_y_red_ball = 300
right = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            movement_red_ball_x = -5
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            movement_red_ball_x = 5
        elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            movement_red_ball_x = 0
        elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            movement_red_ball_x = 0
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP and position_y_red_ball:
            movement_red_ball_y = -5
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            movement_red_ball_y = 5
        elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
            movement_red_ball_y = 0
        elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            movement_red_ball_y = 0
    
    screen.fill(white)
    screen.blit(background, (0,0))
    #pygame.draw.circle(screen, black, (position_x_ball,position_Y_ball), 30)
    screen.blit(soma, (position_x_red_ball, position_y_red_ball))

    if position_x_ball >= 800:
        right = False
        speed = speed + 1
        position_Y_ball = random.randint(0,600)
        winsound.Beep(500,300)
    elif position_x_ball <= 0:
        right = True
        speed = speed + 1
        winsound.Beep(500,300)

    
    if right:
        position_x_ball = position_x_ball + speed
    else:
        position_x_ball = position_x_ball - speed

    pygame.draw.line(screen, black, (30,30), (100,30))

    if position_x_red_ball < 0:
        position_x_red_ball = 0
    elif position_x_red_ball > 800:
        position_x_red_ball = 800
    else:
        position_x_red_ball = position_x_red_ball + movement_red_ball_x

    if position_y_red_ball < 0:
        position_y_red_ball = 0
    elif position_y_red_ball > 600:
        position_y_red_ball = 600
    else:
        position_y_red_ball = position_y_red_ball + movement_red_ball_y



    #pygame.draw.circle(screen, red, (position_x_red_ball,position_y_red_ball), 30)

    pygame.display.update()
    clock.tick(60)
pygame.quit()