from entity import Entity

class Player(Entity):
    def __init__(self):
        self.stats = {
            'health': 300, 
            'attack': 40,
            'magic': 4,
            'speed': 7
        }

        super().__init__(
            self.stats['health'],
            self.stats['attack'],
            self.stats['magic'],
            self.stats['speed']
        )

        