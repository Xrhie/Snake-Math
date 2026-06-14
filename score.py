import pygame
from interface import Drawable

class ScoreManager(Drawable):
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont(None, 32)

    def add_score(self):
        self.score += 1

    def draw(self, screen):
        text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(text, (10, 10))