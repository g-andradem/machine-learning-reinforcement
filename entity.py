class Entity:
    def __init__(self, max_hp, attack, magic, defese, speed):
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack = attack
        self.magic = magic
        self.speed = speed

        self.defese = defese

    def is_alive(self):
        return self.hp > 0
    
    def melee_attack(self, enemy):
        enemy.hp -= self.attack  - enemy.defese

    def magic_attack(self, enemy):
        enemy.hp -= self.magic - enemy.defese

    def heal(self):
        self.hp += self.magic

        if self.hp > self.max_hp:
            self.hp = self.max_hp