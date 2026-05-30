import math
import random
import pygame
from settings import *

class Particle(pygame.sprite.Sprite):
    def __init__(self, pos, velocity, lifetime, color, size):
        super().__init__()
        self.image = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (size, size), size)
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.Vector2(pos)
        self.velocity = velocity
        self.lifetime = lifetime
        self.max_lifetime = lifetime

    def update(self, dt):
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()
            return
        self.pos += self.velocity * dt
        alpha = int(255 * max(0, self.lifetime / self.max_lifetime))
        self.image.set_alpha(alpha)
        self.rect.center = (int(self.pos.x), int(self.pos.y))


def create_explosion(pos, color=(255, 150, 50), count=None,
                     speed=None, lifetime=None):
    if count is None:
        count = PARTICLE_COUNT
    if speed is None:
        speed = PARTICLE_SPEED
    if lifetime is None:
        lifetime = PARTICLE_LIFETIME

    particles = []
    for _ in range(count):
        angle = random.uniform(0, 360)
        speed_var = random.uniform(speed * 0.3, speed)
        vx = math.cos(math.radians(angle)) * speed_var
        vy = -math.sin(math.radians(angle)) * speed_var
        vel = pygame.Vector2(vx, vy)
        size = random.randint(2, 5)
        life = random.uniform(lifetime * 0.5, lifetime)
        p = Particle(pos, vel, life, color, size)
        particles.append(p)
    return particles
