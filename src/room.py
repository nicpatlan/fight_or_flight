class Room():
    def __init__(self, monster):
        self._monster = monster
        self._description = f'generate something descriptive and mention '
        self._occupied = True
        self._loot = ['Scroll', 'Potion']

    def description(self):
        print(self._description + self._monster.description())

    def get_monster(self):
        return self._monster

    def get_occupied(self):
        return self._occupied

    def set_not_occupied(self):
        self._occupied = False
        self._loot.extend(self._monster.get_loot())

    def get_loot(self):
        loot = self._loot
        self._loot = []
        return loot
