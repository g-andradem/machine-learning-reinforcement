from entity import Entity

class Player(Entity):
    def __init__(self):
        self.stats = {
            'health': 300, 
            'attack': 40,
            'magic': 30,
            'defese': 5,
            'speed': 7
        }

        super().__init__(
            max_hp = self.stats['health'],
            attack = self.stats['attack'],
            magic = self.stats['magic'],
            defese = self.stats['defese'],
            speed = self.stats['speed']
        )

        