import pygame
from settings import *
from sprites.tank import Tank
from sprites.target import Target
from sprites.projectile import Projectile
from weapons.bullet_weapon import BulletWeapon
from weapons.rocket_weapon import RocketWeapon
from managers.spawner import Spawner
from managers.collision_manager import CollisionManager
from managers.score_manager import ScoreManager
from ui.hud import HUD

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tank Game")
        self.clock = pygame.time.Clock()
        self.running = True

        self.tank_group = pygame.sprite.Group()
        self.targets_group = pygame.sprite.Group()
        self.projectiles_group = pygame.sprite.Group()
        self.explosions_group = pygame.sprite.Group()

        self.tank = Tank((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.tank.add_weapon(BulletWeapon())
        self.tank.add_weapon(RocketWeapon())
        self.tank_group.add(self.tank)

        self.spawner = Spawner()
        self.collision_manager = CollisionManager()
        self.score_manager = ScoreManager()
        self.hud = HUD(self.tank, self.score_manager)

        self.spawner.spawn(self.targets_group, self.tank.pos, count=3)

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0
            current_time = pygame.time.get_ticks() / 1000.0
            self.handle_events(current_time)
            self.update(dt, current_time)
            self.draw()

    def handle_events(self, current_time):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_1:
                    self.tank.switch_weapon(0)
                elif event.key == pygame.K_2:
                    self.tank.switch_weapon(1)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    projectile = self.tank.fire(current_time)
                    if projectile:
                        self.projectiles_group.add(projectile)

    def update(self, dt, current_time):
        mouse_pos = pygame.mouse.get_pos()
        self.tank.aim(mouse_pos)

        old_pos = pygame.Vector2(self.tank.pos)
        self.tank_group.update(dt)
        if self.collision_manager.resolve_tank_target(self.tank, self.targets_group):
            self.tank.pos = old_pos
            self.tank.rect.center = (int(old_pos.x), int(old_pos.y))

        self.targets_group.update(dt)
        self.projectiles_group.update(dt)
        self.explosions_group.update(dt)
        self.collision_manager.check(
            self.projectiles_group, self.targets_group,
            self.score_manager, self.explosions_group
        )
        self.spawner.update(dt, self.targets_group, self.tank.pos)

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.targets_group.draw(self.screen)
        self.tank_group.draw(self.screen)
        self.tank.draw_turret(self.screen)
        self.projectiles_group.draw(self.screen)
        self.explosions_group.draw(self.screen)
        self.hud.draw(self.screen)
        pygame.display.flip()
