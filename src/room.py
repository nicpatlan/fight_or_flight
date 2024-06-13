import random
ROOM_LIST = ['The room is nearly pitch black but you hear the rumbling of what sounds like a ',
             'You find yourself in a dimly lit room, crouching in the corner you see a ',
             'The room is so bright from a blazing fire centered in the room you nearly dont see an ',
             'Several torches line a corridor, around the corner you spot a ',
             'The room appears to be a barracks of some kind and sitting at a table you see a ',
             'You notice little about the room before being confronted by ']


class Room():
    def __init__(self, monster, loot):
        self._monster = monster
        self._description = ROOM_LIST[random.randrange(6)]
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
