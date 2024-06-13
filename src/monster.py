from entity import Entity

MONSTER_LIST = [('kobold', 2, 1, 1),
                ('goblin', 3, 2, 1),
                ('gnoll', 5, 2, 2),
                ('orc', 6, 3, 2),
                ('bugbear', 7, 3, 3),
                ('drake', 8, 4, 4)] 

def generate_monster(random_val, level, att_mod, def_mod, loot): 
    attribute = MONSTER_LIST[random_val]
    if level == 0:
        level = 1
    return Monster(attribute[0],
                   level,
                   attribute[1] * level,
                   attribute[2] * level + att_mod,
                   attribute[3] * level + def_mod,
                   loot)

class Monster(Entity):
    def __init__(self, name, level, hp, attack, defense, loot):
        super().__init__(name, level, hp, attack, defense)
        self._xp_gain = level if level == 1 else level // 2
        self._loot = loot

    def description(self):
        return f'{self.get_name()}'

    def get_xp_gain(self):
        return self._xp_gain

    def get_loot(self):
        loot = self._loot
        self._loot = []
        return loot
