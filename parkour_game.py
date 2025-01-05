
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Parkour Thief Chase")

# Clock for frame rate
clock = pygame.time.Clock()
FPS = 60

# Load assets
# Uncomment and replace with image paths if available
# boy_img = pygame.image.load("boy.png")
# police_img = pygame.image.load("police.png")
# dog_img = pygame.image.load("dog.png")

# Boy class
class Boy:
    def __init__(self):
        self.x = 50
        self.y = 300
        self.width = 40
        self.height = 60
        self.velocity = 5
        self.jump = False
        self.jump_count = 10

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - self.width:
            self.x += self.velocity
        if not self.jump:
            if keys[pygame.K_SPACE]:
                self.jump = True
        else:
            if self.jump_count >= -10:
                neg = 1 if self.jump_count > 0 else -1
                self.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.jump = False
                self.jump_count = 10


# Police class
class Police:
    def __init__(self):
        self.x = 0
        self.y = 300
        self.width = 40
        self.height = 60
        self.velocity = 3

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))
        self.x += self.velocity


# Hurdle class
class Hurdle:
    def __init__(self):
        self.x = random.randint(SCREEN_WIDTH // 2, SCREEN_WIDTH)
        self.y = 310
        self.width = 20
        self.height = 40

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))

    def move(self):
        self.x -= 5
        if self.x < -self.width:
            self.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 100)


# Main game function
def main():
    run = True
    boy = Boy()
    police = Police()
    hurdles = [Hurdle() for _ in range(3)]

    while run:
        clock.tick(FPS)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        boy.move(keys)

        # Draw boy, police, and hurdles
        boy.draw()
        police.draw()
        for hurdle in hurdles:
            hurdle.draw()
            hurdle.move()

        # Check for collisions
        for hurdle in hurdles:
            if (
                boy.x < hurdle.x + hurdle.width
                and boy.x + boy.width > hurdle.x
                and boy.y < hurdle.y + hurdle.height
                and boy.y + boy.height > hurdle.y
            ):
                print("Game Over!")
                run = False

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
