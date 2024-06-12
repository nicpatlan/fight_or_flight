class Room():
    def __init__(self):
        self._description = "generate something descriptive"
        self._monster = Monster()
        self._occupied = True
        self._loot = [Scroll(), Potion()]

    def description(self):
        print(self._description)

    def get_monster(self):
        return self._monster

    def get_occupied(self):
        return self._occupied

    def set_not_occupied(self):
        self._occupied = False
        self._loot.extend(self._monster.get_loot())

    def get_loot(self):
        return self._loot
