import math
import pygame
from weapons.weapon import Weapon
from sprites.projectile import Projectile
from settings import *

class RocketWeapon(Weapon):
    def __init__(self):
        super().__init__(fire_rate=ROCKET_FIRE_RATE, damage=ROCKET_DAMAGE, name="Rocket")

    def create_projectile(self, pos, angle):
        dx = math.cos(math.radians(angle))
        dy = -math.sin(math.radians(angle))
        velocity = pygame.Vector2(dx, dy) * ROCKET_SPEED
        spawn_x = pos[0] + dx * (TANK_TURRET_LENGTH + 5)
        spawn_y = pos[1] + dy * (TANK_TURRET_LENGTH + 5)
        return Projectile(
            (spawn_x, spawn_y), velocity, self.damage,
            ROCKET_RADIUS, ROCKET_COLOR, ROCKET_LIFETIME,
            splash_radius=ROCKET_SPLASH_RADIUS,
            splash_damage=ROCKET_SPLASH_DAMAGE
        )
