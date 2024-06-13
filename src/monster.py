from entity import Entity

class Monster(Entity):
    def __init__(self, name, level, hp, attack, defense, loot):
        super().__init__(name, level, hp, attack, defense)
        self._xp_gain = level
        self._loot = loot

    def description(self):
        return f'a {self.get_name()}'

    def get_xp_gain(self):
        return self._xp_gain

    def get_loot(self):
        loot = self._loot
        self._loot = []
        return loot
