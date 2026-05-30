import pygame
from settings import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos, velocity, damage, radius, color, lifetime,
                 splash_radius=0, splash_damage=0):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.Vector2(pos)
        self.velocity = velocity
        self.damage = damage
        self.lifetime = lifetime
        self.splash_radius = splash_radius
        self.splash_damage = splash_damage

    def update(self, dt):
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()
            return
        self.pos += self.velocity * dt
        self.rect.center = (int(self.pos.x), int(self.pos.y))
