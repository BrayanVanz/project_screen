import pygame
import winsound
import random

pygame.init()

size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Castlevania Rise of Sorrow")
clock = pygame.time.Clock()
soma = pygame.image.load("AriaSoma_Sprite.png")
pygame.display.set_icon(soma)


def game_over():
    white = (255,255,255)
    black = (0,0,0)
    background = pygame.image.load("grave.jpg")
    running = True
    #pygame.mixer.music.load()
    #pygame.mixer.music.play(1)
    font = pygame.font.Font(None, 86)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN and event.key== pygame.K_ESCAPE:
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
                game()
        screen.fill(white)
        screen.blit(background, (0, -300))
    
        text = font.render("Press F1 to retry: ", True, white)
        screen.blit(text, (10, 500))
        pygame.display.update()
        clock.tick(60)

def game():
    size = (800,600)
    white = (255,255,255)
    black = (0,0,0)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size)
    running = True
    position_x_ball = 0
    position_Y_ball = 300
    soma = pygame.image.load("AriaSoma_Sprite.png")
    soma_original = pygame.image.load("AriaSoma_Sprite.png")
    dracula_original = pygame.image.load("Dracula.png")
    background = pygame.image.load("castle.png")
    pygame.display.set_caption("Castlevania Rise of Sorrow")
    pygame.display.set_icon(soma)
    speed = 1
    position_x_red_ball = 400
    movement_red_ball_x = 0
    movement_red_ball_y = 0
    position_y_red_ball = 300
    right = True
    pygame.mixer.music.load("VK.mp3")
    pygame.mixer.music.play(-1)
    font = pygame.font.Font(None, 36)
    points = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                movement_red_ball_x = -5
                soma = pygame.transform.flip(soma,True,False)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                movement_red_ball_x = 5
                soma = soma_original
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
        screen.blit(dracula_original, (position_x_ball, position_Y_ball))

        if position_x_ball >= 700:
            right = False
            points += 1
            speed = speed + 1
            position_Y_ball = random.randint(0,600)
            winsound.Beep(500,300)
        elif position_x_ball <= 0:
            right = True
            points += 1
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

        pixel_x_soma = list(range(position_x_red_ball, position_x_red_ball + 50))
        pixel_y_soma = list(range(position_y_red_ball, position_y_red_ball + 100))
        pixel_x_dracula = list(range(position_x_ball, position_x_ball + 100))
        pixel_y_dracula = list(range(position_Y_ball, position_Y_ball + 144))

        total_pixels_height = len(list(set(pixel_y_soma) & set(pixel_y_dracula)))
        total_pixels_width = len(list(set(pixel_x_soma) & set(pixel_x_dracula)))

        if total_pixels_height > 12:
            if total_pixels_width > 18:
                running = False
                game_over()


        text = font.render(f"Points: {points}", True, white)
        screen.blit(text, (10, 10))

        pygame.display.update()
        clock.tick(60)

game()
pygame.quit()