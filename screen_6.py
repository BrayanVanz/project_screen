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
    pygame.draw.circle(screen, black, (80,50), 30)
    pygame.draw.circle(screen, white, (80,50), 28)
    pygame.draw.line(screen, black, (90,75), (150,350))
    pygame.draw.circle(screen, black, (150,350), 30)
    pygame.draw.circle(screen, white, (150,350), 28)
    pygame.draw.line(screen, black, (180, 340), (380,280))
    pygame.draw.circle(screen, black, (380,280), 30)
    pygame.draw.circle(screen, white, (380,280), 28)
    pygame.draw.line(screen, black, (410,280), (510,280))
    pygame.draw.circle(screen, black, (510,280), 30)
    pygame.draw.circle(screen, white, (510,280), 28)

    pygame.display.update()
pygame.quit()