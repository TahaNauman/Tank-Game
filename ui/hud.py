import pygame
from settings import *

class HUD:
    def __init__(self, tank, score_manager):
        self.tank = tank
        self.score_manager = score_manager
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.tiny_font = pygame.font.Font(None, 18)

    def draw(self, screen):
        score_text = self.font.render(
            f"Score: {self.score_manager.get_score()}", True, WHITE
        )
        screen.blit(score_text, (10, 10))

        hp_x = 10
        hp_y = 50
        bar_width = 120
        bar_height = 16
        health_ratio = max(0, self.tank.health / self.tank.max_health)

        hp_label = self.small_font.render("HP", True, WHITE)
        screen.blit(hp_label, (hp_x, hp_y))

        bar_x = hp_x + 30
        bar_y = hp_y
        pygame.draw.rect(screen, (60, 0, 0), (bar_x, bar_y, bar_width, bar_height))
        fill_width = int(bar_width * health_ratio)
        if health_ratio > 0.5:
            bar_color = GREEN
        elif health_ratio > 0.25:
            bar_color = (255, 220, 50)
        else:
            bar_color = RED
        pygame.draw.rect(screen, bar_color, (bar_x, bar_y, fill_width, bar_height))
        pygame.draw.rect(screen, WHITE, (bar_x, bar_y, bar_width, bar_height), 2)

        weapon_name = self.tank.weapon.name if self.tank.weapon else "None"
        weapon_text = self.small_font.render(
            f"Weapon: {weapon_name}  [1] [2]", True, (200, 200, 100)
        )
        screen.blit(weapon_text, (10, 80))

        controls = self.tiny_font.render(
            "WASD: Move | LMB: Shoot | 1/2: Weapon | ESC: Quit",
            True, (150, 150, 150)
        )
        screen.blit(controls, (10, SCREEN_HEIGHT - 30))
