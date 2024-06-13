class Room():
    def __init__(self, monster, loot):
        self._monster = monster
        self._description = f'generate something descriptive and mention '
        self._occupied = True
        self._loot = loot

    def description(self):
        print(self._description + self._monster.description())

    def get_monster(self):
        return self._monster

    def get_occupied(self):
        return self._occupied

    def set_not_occupied(self):
        self._occupied = False
        if self._monster is not None:
            self._loot.extend(self._monster.get_loot())

    def get_loot(self):
        loot = self._loot
        self._loot = []
        return loot
