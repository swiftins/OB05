
import pygame
pygame.init()

window_size = (900, 900)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Test Project")

image = pygame.image.load("virus.jpg")
image_rect = image.get_rect()

speed = 1

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect.x = mouseX
            image_rect.y = mouseY
     

    screen.fill((0,0,255))
    screen.blit(image,image_rect)

    pygame.display.flip()
pygame.quit() 