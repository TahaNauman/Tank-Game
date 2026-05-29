import pygame
from settings import *

class Target(pygame.sprite.Sprite):
    def __init__(self, pos, size, color, health):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        pygame.draw.rect(self.image, TARGET_BORDER_COLOR, self.image.get_rect(), 3)
        pygame.draw.line(self.image, TARGET_BORDER_COLOR, (2, 2), (size - 2, size - 2), 2)
        pygame.draw.line(self.image, TARGET_BORDER_COLOR, (size - 2, 2), (2, size - 2), 2)

        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.Vector2(pos)
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()
            return True
        return False
