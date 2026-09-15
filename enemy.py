from entity import Entity

class Enemy(Entity):
    def __init__(self, speed_enemy):
        self.stats = {
            'health': 300, 
            'attack': 35,
            'magic': 40,
            'speed': 6 + speed_enemy
        }

        super().__init__(
            self.stats['health'],
            self.stats['attack'],
            self.stats['magic'],
            self.stats['speed']
        )