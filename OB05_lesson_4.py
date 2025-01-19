import pygame
pygame.init()

# Настройка окна
window_size = (900, 900)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Test Project")

# Загрузка изображений
image = pygame.image.load("virus.jpg")
image_rect = image.get_rect()

image2 = pygame.image.load("car_foto.png")
image_rect2 = image2.get_rect()

# Позиционируем второе изображение
image_rect2.topleft = (400, 400)

# Скорость движения
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

    # Проверка на пересечение
    if image_rect.colliderect(image_rect2):
        print("Заходим в зону")

    # Отрисовка экрана
    screen.fill((0, 0, 255))
    screen.blit(image, image_rect)
    screen.blit(image2, image_rect2)

    pygame.display.flip()

pygame.quit()
