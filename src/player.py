import random
from entity import Entity
from items import use_item, ITEM_LIST

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
        print(f'Hitpoints: {self.get_hp()}')
        print(f'Attack: {self.get_attack()}')
        print(f'Defense: {self.get_defense()}')
        print(f'XP: {self.get_xp()}')
        print(f'Next Level: {self.get_xp_to_level()}')

    def prompt_action(self):
        print('What will you do?')
        print('fight, flight, advance, loot, item, or status')
        print_break()
        action = input()
        return action

    def prompt_item_action(self, monster):
            while True:
                print('Which item would you like to use?')
                print(f'{self.get_inventory()}')
                print(f'or type back')
                print_break()
                item_action = input()
                if self.check_inventory(item_action):
                    self.remove_item(item_action)
                    use_item(self, monster, item_action)
                    print_break()
                    return True
                elif item_action == 'back':
                    return False
                else:
                    print('You do not have that item.')

    def fight_round(self, monster, item=False):
        if not item:
            damage = self.get_attack() - monster.get_defense()
            if damage < 0:
                damage = 0
            monster.dec_hp(damage)
            print(f'You attack dealing {damage} damage!')
            if monster.is_alive():
                print(f'{monster.get_name()} now has {monster.get_hp()} hitpoints')
            print_break()
        if monster.is_alive():
            damage = monster.get_attack() - self.get_defense()
            if damage < 0:
                damage = 0
            print(f'{monster.get_name()} attacks you for {damage} damage!')
            self.dec_hp(damage)
            if self.is_alive():
                print(f'You have {self.get_hp()} hp remaining!')
                print_break()
        else:
            print(f'You have slain a monster!')
            xp = monster.get_xp_gain()
            self.inc_xp(xp)
            print(f'A {monster.get_name()} now lies before you.')
            print_break()
        if not self.is_alive():
            print(f'You have been slain by a {monster.get_name()}!')
            print_break()
