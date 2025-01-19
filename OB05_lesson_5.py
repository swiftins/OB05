import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Цвета
BLACK = (0, 0, 0)
WHITE = (100, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 255)

# Классы
class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 20
        self.x = (WINDOW_WIDTH - self.width) // 2
        self.y = WINDOW_HEIGHT - 50
        self.speed = 10

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WINDOW_WIDTH - self.width:
            self.x += self.speed

class Ball:
    def __init__(self):
        self.radius = 10
        self.x = WINDOW_WIDTH // 2
        self.y = WINDOW_HEIGHT // 2
        self.speed_x = random.choice([-4, 4])
        self.speed_y = -4

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Отскок от стен
        if self.x <= 0 or self.x >= WINDOW_WIDTH:
            self.speed_x = -self.speed_x
        if self.y <= 0:
            self.speed_y = -self.speed_y

class Brick:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.active = True

    def draw(self, screen):
        if self.active:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Основной игровой класс
class ArkanoidGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Arkanoid")
        self.clock = pygame.time.Clock()
        self.paddle = Paddle()
        self.ball = Ball()
        self.bricks = self.create_bricks()
        self.running = True

    def create_bricks(self):
        bricks = []
        brick_width = 70
        brick_height = 20
        rows = 5
        cols = 10
        spacing = 5

        for row in range(rows):
            for col in range(cols):
                x = col * (brick_width + spacing) + spacing
                y = row * (brick_height + spacing) + spacing
                bricks.append(Brick(x, y, brick_width, brick_height, BLUE))

        return bricks

    def check_collisions(self):
        # Проверка столкновения мяча с платформой
        if (
            self.paddle.y <= self.ball.y + self.ball.radius <= self.paddle.y + self.paddle.height
            and self.paddle.x <= self.ball.x <= self.paddle.x + self.paddle.width
        ):
            self.ball.speed_y = -self.ball.speed_y

        # Проверка столкновения мяча с кирпичами
        for brick in self.bricks:
            if brick.active and brick.x <= self.ball.x <= brick.x + brick.width and brick.y <= self.ball.y <= brick.y + brick.height:
                self.ball.speed_y = -self.ball.speed_y
                brick.active = False
                break

        # Проверка проигрыша
        if self.ball.y > WINDOW_HEIGHT:
            self.running = False

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            self.paddle.move(keys)
            self.ball.move()
            self.check_collisions()

            self.paddle.draw(self.screen)
            self.ball.draw(self.screen)
            for brick in self.bricks:
                brick.draw(self.screen)

            pygame.display.flip()

        pygame.quit()

# Запуск игры
if __name__ == "__main__":
    game = ArkanoidGame()
    game.run()
