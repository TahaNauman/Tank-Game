class Weapon:
    def __init__(self, fire_rate, damage, name="Weapon"):
        self.fire_rate = fire_rate
        self.damage = damage
        self.name = name
        self.last_shot_time = -fire_rate

    def can_fire(self, current_time):
        return current_time - self.last_shot_time >= self.fire_rate

    def fire(self, pos, angle, current_time):
        if not self.can_fire(current_time):
            return None
        self.last_shot_time = current_time
        return self.create_projectile(pos, angle)

    def create_projectile(self, pos, angle):
        raise NotImplementedError
