class Entity:
    def __init__(self, max_hp, attack, speed):
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack = attack
        self.speed = speed

        # vulnerable
        self.vulnerable = True

    def is_alive(self):
            return self.hp > 0
    
    def attack_enemy(self, enemy):
        self.vulnerable = True
        if enemy.vulnerable:
            enemy.hp -= self.attack

    def heal(self):
        self.hp += 20

        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def defend(self):
        self.vulnerable = False