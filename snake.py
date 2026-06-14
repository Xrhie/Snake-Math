import pygame
from interface import Drawable, Movable

CELL_SIZE = 20

class Snake (Drawable, Movable):
    def __init__(self, data):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = "RIGHT"

        self.color = data["color"]

        self.head_img = pygame.image.load(data["img"])
        self.head_img = pygame.transform.scale(self.head_img, (CELL_SIZE, CELL_SIZE))

    def change_direction(self, keys):
        if keys[pygame.K_UP] and self.direction != "DOWN":
            self.direction = "UP"
        elif keys[pygame.K_DOWN] and self.direction != "UP":
            self.direction = "DOWN"
        elif keys[pygame.K_LEFT] and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif keys[pygame.K_RIGHT] and self.direction != "LEFT":
            self.direction = "RIGHT"

    def move(self):
        x, y = self.body[0]
        if self.direction == "UP":
            y -= CELL_SIZE
        elif self.direction == "DOWN":
            y += CELL_SIZE
        elif self.direction == "LEFT":
            x -= CELL_SIZE
        elif self.direction == "RIGHT":
            x += CELL_SIZE

        self.body.insert(0, (x, y))
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def head_position(self):
        return self.body[0]

    def check_collision(self):
        x, y = self.head_position()
        if x < 0 or x >= 600 or y < 0 or y >= 600:
            return True
        if self.body[0] in self.body[1:]:
            return True
        return False

    def draw(self, screen):
        for i, segment in enumerate(self.body):
            x, y = segment

            if i == 0:
                screen.blit(self.head_img, (x, y))  # kepala pakai gambar
            else:
                pygame.draw.rect(screen, self.color, (x, y, CELL_SIZE, CELL_SIZE))  # badan warna