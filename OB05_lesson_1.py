import pygame
pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Test Project")
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((0,0,255))
    pygame.display.flip()
pygame.quit()