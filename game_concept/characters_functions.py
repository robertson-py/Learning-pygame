class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.strenght = 5
        self.defense = 2
        self.energy = 100
        self.armor = 1
        self.exp = 0
        self.mana = 10
        self.poison = False
        self.level = 1

    def walk(self, terrain):
        self.energy -= terrain.type    # Create class terrain or related: terrain.type

    def attacking(self, weapon, enemy):
        self.strenght += weapon    # Create class ewapon or related: weapon
        if self.strenght > enemy.defense:
            self.exp += (self.strenght - enemy.defense)    # Create class enemy or related: enemy_defense 
            if self.exp == 25:
                Character.level_up()

    def defending(self, shield, enemy_attack):
        self.defense += shield + self.armor
        if self.defense >= enemy_attack:    # Create class enemy or related: enemy_attack 
            self.hp -= 1
        elif self.defense < enemy_attack:
            self.hp -= (enemy_attack-self.defense)

    def magic_attack(self, spell):
        self.mana -= spell.mana    # Create class spell or related: spell.mana
    
    def level_up(self):
        k = 25
        if self.exp >= k:
            self.level += 1
            k += k*2
        return "You gain a level!"
