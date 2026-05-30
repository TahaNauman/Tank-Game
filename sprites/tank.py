import pygame
import math
from settings import *

class Tank(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((TANK_WIDTH, TANK_HEIGHT))
        self.image.fill(TANK_COLOR)
        pygame.draw.rect(self.image, TANK_TRACK_COLOR, (0, 0, 6, TANK_HEIGHT))
        pygame.draw.rect(self.image, TANK_TRACK_COLOR, (TANK_WIDTH - 6, 0, 6, TANK_HEIGHT))
        pygame.draw.rect(self.image, (40, 100, 40), self.image.get_rect(), 2)

        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.Vector2(pos)
        self.angle = 0.0
        self.health = TANK_HEALTH
        self.max_health = TANK_HEALTH
        self.weapons = []
        self.current_weapon_index = 0

    @property
    def weapon(self):
        if self.weapons:
            return self.weapons[self.current_weapon_index]
        return None

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def switch_weapon(self, index):
        if 0 <= index < len(self.weapons):
            self.current_weapon_index = index

    def update(self, dt):
        keys = pygame.key.get_pressed()
        dx = (keys[pygame.K_d] - keys[pygame.K_a]) * TANK_SPEED * dt
        dy = (keys[pygame.K_s] - keys[pygame.K_w]) * TANK_SPEED * dt
        self.pos.x += dx
        self.pos.y += dy
        self.pos.x = max(TANK_WIDTH // 2, min(SCREEN_WIDTH - TANK_WIDTH // 2, self.pos.x))
        self.pos.y = max(TANK_HEIGHT // 2, min(SCREEN_HEIGHT - TANK_HEIGHT // 2, self.pos.y))
        self.rect.center = (int(self.pos.x), int(self.pos.y))

    def aim(self, mouse_pos):
        dx = mouse_pos[0] - self.pos.x
        dy = mouse_pos[1] - self.pos.y
        self.angle = math.degrees(math.atan2(-dy, dx))

    def draw_turret(self, surface):
        dx = math.cos(math.radians(self.angle))
        dy = -math.sin(math.radians(self.angle))
        start_x = self.pos.x - dx * 4
        start_y = self.pos.y - dy * 4
        end_x = self.pos.x + dx * TANK_TURRET_LENGTH
        end_y = self.pos.y + dy * TANK_TURRET_LENGTH
        pygame.draw.line(surface, TANK_TURRET_COLOR,
                         (int(start_x), int(start_y)),
                         (int(end_x), int(end_y)),
                         TANK_TURRET_WIDTH)
        pygame.draw.circle(surface, (255, 200, 50),
                           (int(end_x), int(end_y)), 3)

    def fire(self, current_time):
        if self.weapon:
            return self.weapon.fire((self.pos.x, self.pos.y), self.angle, current_time)
        return None
