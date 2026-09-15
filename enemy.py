from entity import Entity

class Enemy(Entity):
    def __init__(self):
        self.stats = {
            'health': 300, 
            'attack': 30,
            'magic': 5,
            'speed': 6
        }

        super().__init__(
            self.stats['health'],
            self.stats['attack'],
            self.stats['magic'],
            self.stats['speed']
        )