from entity import Entity

class Enemy(Entity):
    def __init__(self, speed_enemy):
        self.stats = {
            'health': 300, 
            'attack': 35,
            'magic': 40,
            'defese': 2,
            'speed': 6 + speed_enemy
        }

        super().__init__(
            max_hp = self.stats['health'],
            attack = self.stats['attack'],
            magic = self.stats['magic'],
            defese = self.stats['defese'],
            speed = self.stats['speed']
        )