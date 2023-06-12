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
    pygame.draw.circle(screen, black, (400,300), 100)
    pygame.draw.line(screen, black, (0,600), (800,0))
    pygame.draw.circle(screen, white, (400,300), 98)


    pygame.display.update()
pygame.quit()