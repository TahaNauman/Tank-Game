import pygame
from settings import *
from sprites.explosion import create_explosion

class CollisionManager:
    def check(self, projectiles_group, targets_group, score_manager,explosions_group):
        hits = pygame.sprite.groupcollide(projectiles_group, targets_group, True, False)

        for projectile, hit_targets in hits.items():
            for target in hit_targets:
                destroyed = target.take_damage(projectile.damage)
                if destroyed:
                    score_manager.add_score(TARGET_SCORE)

            if projectile.splash_radius > 0:
                for target in list(targets_group):
                    dist = projectile.pos.distance_to(target.pos)
                    if dist <= projectile.splash_radius:
                        destroyed = target.take_damage(projectile.splash_damage)
                        if destroyed:
                            score_manager.add_score(TARGET_SCORE)
                explosions_group.add(*create_explosion(projectile.pos, color=(255, 150, 50)))

    def resolve_tank_target(self, tank, targets_group):
        hits = pygame.sprite.spritecollide(tank, targets_group, False)
        return len(hits) > 0
