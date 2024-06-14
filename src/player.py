import random
from entity import Entity

class Player(Entity):
    def __init__(self, name, level, hp, attack, defense):
        super().__init__(name, level, hp, attack, defense)
        self._xp = 0
        self._xp_to_level = level
        self._inventory = []

    def level_up(self, amount):
        self._level += amount
        self.inc_max_hp(amount * 2)
        self._hp = self._max_hp
        if random.randrange(2) == 0:
            self.inc_attack(amount)
        else:
            self.inc_defense(amount)

    def get_xp(self):
        return self._xp

    def inc_xp(self, amount):
        self._xp += amount
        print(f'You gained {amount} xp.')
        gained_levels = 0
        if self._xp >= self._xp_to_level:
            while self._xp >= self._xp_to_level:
                gained_levels += 1
                self._xp -= self._xp_to_level
                self._xp_to_level += 1
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
        for idx, element in enumerate(self._inventory):
            if item == element[0].get_name():
                return idx
        return -1

    def remove_item(self, item):
        idx = self.check_inventory(item)
        if idx >= 0:
            if self._inventory[idx][1] > 1:
                number = self._inventory[idx][1] - 1
                element = self._inventory[idx][0]
                self._inventory[idx] = (element, number)
                return self._inventory[idx][0]
            else:
                item_tuple = self._inventory.pop(idx)
                return item_tuple[0]

    def receive_loot(self, items):
        for item in items:
            idx = self.check_inventory(item.get_name())
            if idx >= 0:
                number = self._inventory[idx][1] + 1
                self._inventory[idx] = (item, number)
            else:
                self._inventory.append((item, 1))

    def status(self):
        print(f'Player: {self.get_name()}')
        print(f'Level: {self.get_level()}')
        print(f'Hitpoints: {self.get_hp()}/{self.get_max_hp()}')
        print(f'Attack: {self.get_attack()}')
        print(f'Defense: {self.get_defense()}')
        print(f'XP: {self.get_xp()}/{self.get_xp_to_level()}')
