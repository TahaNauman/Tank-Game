import random
import math
from settings import *
from sprites.target import Target

class Spawner:
    def __init__(self):
        self.timer = 0.0

    def update(self, dt, targets_group, tank_pos=None):
        if len(targets_group) >= MAX_TARGETS:
            return
        self.timer += dt
        if self.timer >= SPAWN_INTERVAL:
            self.timer = 0.0
            self.spawn(targets_group, tank_pos)

    def spawn(self, targets_group, tank_pos=None, count=1):
        for _ in range(count):
            for attempt in range(30):
                x = random.randint(TARGET_SIZE, SCREEN_WIDTH - TARGET_SIZE)
                y = random.randint(TARGET_SIZE, SCREEN_HEIGHT - TARGET_SIZE)

                if tank_pos:
                    dist = math.hypot(x - tank_pos[0], y - tank_pos[1])
                    if dist < 120:
                        continue

                too_close = False
                for target in targets_group:
                    if math.hypot(x - target.pos.x, y - target.pos.y) < 50:
                        too_close = True
                        break
                if too_close:
                    continue

                size_var = random.choice([TARGET_SIZE, TARGET_SIZE - 4, TARGET_SIZE + 4])
                target = Target((x, y), size_var, TARGET_COLOR, TARGET_HEALTH)
                targets_group.add(target)
                break
