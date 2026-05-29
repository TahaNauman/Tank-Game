import math
import pygame
from weapons.weapon import Weapon
from sprites.projectile import Projectile
from settings import *

class BulletWeapon(Weapon):
    def __init__(self):
        super().__init__(fire_rate=BULLET_FIRE_RATE, damage=BULLET_DAMAGE)

    def create_projectile(self, pos, angle):
        dx = math.cos(math.radians(angle))
        dy = -math.sin(math.radians(angle))
        velocity = pygame.Vector2(dx, dy) * BULLET_SPEED
        spawn_x = pos[0] + dx * (TANK_TURRET_LENGTH + 5)
        spawn_y = pos[1] + dy * (TANK_TURRET_LENGTH + 5)
        return Projectile(
            (spawn_x, spawn_y), velocity, self.damage,
            BULLET_RADIUS, BULLET_COLOR, BULLET_LIFETIME
        )
