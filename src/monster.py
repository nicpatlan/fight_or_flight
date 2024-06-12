from entity import Entity

class Monster(Entity):
    def __init__(self, name, level, hp, attack, defense):
        super().__init__(name, level, hp, attack, defense)
        self._loot = ['Gold']

    def description(self):
        return f'a {self.get_name()}'

    def get_loot(self):
        loot = self._loot
        self._loot = []
        return loot
