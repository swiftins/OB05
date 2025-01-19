# Мой космонавт (kosm) отправился в полет по голубому небу. На пути у него космческий барьер (barrier),  
# при соприкосновении с которым
# космонавт теряет над собой контроль. Барьер  его отталкивет и переворачивает. Небо краснеет. 
# Но как только космонавт отталкивается от  барьера, все возвращается на свои места и он благополучно 
#плывет дальше по голубому небу.

import pygame
pygame.init()


window_size = (900, 900)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("My cosmo game")


image = pygame.image.load("kosm.png")
image_rect = image.get_rect()

image2 = pygame.image.load("barrier.jpg")
image_rect2 = image2.get_rect()


image_rect2.topleft = (400, 400)

angle = 0

background_color = (0, 0, 255)  

in_space_zone = False

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect.x = mouseX
            image_rect.y = mouseY

    if image_rect.colliderect(image_rect2):
        if not in_space_zone:  
            print("врезался в космический барьер")
            angle = 180  
            background_color = (255, 0, 0)  
            in_space_zone = True
    else:
        if in_space_zone:  
            print("врезался в космический барьер")
            angle = 0  
            background_color = (0, 0, 255) 
            in_space_zone = False

    
    screen.fill(background_color)

 
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=image_rect.center)

    
    screen.blit(rotated_image, rotated_rect)
    screen.blit(image2, image_rect2)

    pygame.display.flip()

pygame.quit()
