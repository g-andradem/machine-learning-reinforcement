class Entity:
    def __init__(self, max_hp, attack, magic, speed):
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack = attack
        self.magic = magic
        self.speed = speed

        # vulnerable
        self.vulnerable = True

    def is_alive(self):
            return self.hp > 0
    
    def melee_attack(self, enemy):
        self.vulnerable = True
        if enemy.vulnerable:
            enemy.hp -= self.attack

    def magic_attack(self, enemy):
        self.vulnerable = True
        if enemy.vulnerable:
            enemy.hp -= self.magic

    def heal(self):
        self.hp += 20

        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def defend(self):
        self.vulnerable = False