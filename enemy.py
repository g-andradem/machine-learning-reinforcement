from entity import Entity

class Enemy(Entity):
    def __init__(self, max_hp, attack, speed):
        super().__init__(max_hp, attack, speed)