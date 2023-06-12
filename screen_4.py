import pygame

pygame.init()
size = (800,600)
white = (255,255,255)
black = (0,0,0)
screen = pygame.display.set_mode(size)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    
    screen.fill(white)
    pygame.draw.line(screen, black, (0,300), (800,300))
    pygame.draw.line(screen, black, (100, 500), (100, 100))
    pygame.draw.line(screen, black, (101, 100), (200, 350))
    pygame.draw.line(screen, black, (201,350), (250,120))
    pygame.draw.line(screen, black, (251,120), (251,450))
    pygame.draw.line(screen, black, (252,450), (450,80))
    pygame.draw.line(screen, black, (451,80), (720,400))

    pygame.display.update()
pygame.quit()