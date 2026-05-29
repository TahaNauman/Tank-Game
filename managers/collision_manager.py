import pygame
from settings import *

class CollisionManager:
    def check(self, projectiles_group, targets_group, score_manager):
        hits = pygame.sprite.groupcollide(
            projectiles_group, targets_group, True, False
        )
        for projectile, hit_targets in hits.items():
            for target in hit_targets:
                destroyed = target.take_damage(projectile.damage)
                if destroyed:
                    score_manager.add_score(TARGET_SCORE)

    def resolve_tank_target(self, tank, targets_group):
        hits = pygame.sprite.spritecollide(tank, targets_group, False)
        return len(hits) > 0
