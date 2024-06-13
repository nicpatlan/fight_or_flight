import random
from entity import Entity
from items import ITEM_LIST

def print_break():
    print('=============================================')
    print('')

class Player(Entity):
    def __init__(self, name, level, hp, attack, defense):
        super().__init__(name, level, hp, attack, defense)
        self._xp = 0
        self._xp_to_level = level   # TODO adjust this amount
        self._inventory = [ITEM_LIST[0],
                           ITEM_LIST[1],
                           ITEM_LIST[2],
                           ITEM_LIST[3],
                           ITEM_LIST[4],
                           ITEM_LIST[5]]

    def level_up(self, amount):
        self._level += amount
        self.inc_max_hp(amount * 2)
        self._hp = self._max_hp
        self._xp_to_level = self.get_level()  # TODO adjust these too
        if random.randrange(2) == 0:
            self.inc_attack(amount)
        else:
            self.inc_defense(amount)

    def get_xp(self):
        return self._xp

    def inc_xp(self, amount):
        self._xp += amount
        print(f'You gained {amount} xp.')
        if self._xp >= self._xp_to_level:
            gained_levels = self._xp // self._xp_to_level
            self._xp %= self._xp_to_level
            self.level_up(gained_levels)
            print(f'Your level increased!')
            print(f'You are now level {self.get_level()}.')
        else:
            print(f'You have {self.get_xp()} total xp.')

    def get_xp_to_level(self):
        return self._xp_to_level

    def get_inventory(self):
        return self._inventory

    def check_inventory(self, item):
        return item in self._inventory

    def remove_item(self, item):
        self._inventory.remove(item)

    def receive_loot(self, items):
        self._inventory.extend(items)

    def status(self):
        print(f'Player: {self.get_name()}')
        print(f'Level: {self.get_level()}')
        print(f'Hitpoints: {self.get_hp()}/{self.get_max_hp()}')
        print(f'Attack: {self.get_attack()}')
        print(f'Defense: {self.get_defense()}')
        print(f'XP: {self.get_xp()}/{self.get_xp_to_level()}')
