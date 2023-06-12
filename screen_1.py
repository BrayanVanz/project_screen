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

    pygame.display.update()
pygame.quit()