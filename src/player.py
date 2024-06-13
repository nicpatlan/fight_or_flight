from entity import Entity
from items import use_item, ITEM_LIST

def print_break():
    print('=============================================')
    print('')

class Player(Entity):
    def __init__(self, name, level, hp, attack, defense):
        super().__init__(name, level, hp, attack, defense)
        self._xp = 0
        self._inventory = [ITEM_LIST[0],
                           ITEM_LIST[1],
                           ITEM_LIST[2],
                           ITEM_LIST[3],
                           ITEM_LIST[4],
                           ITEM_LIST[5]]

    def level_up(self, amount):
        self._level += amount
        self.inc_max_hp(amount * 10)
        self._hp = self._max_hp
        self.inc_attack(amount * 2)
        self.inc_defense(amount * 2)

    def get_xp(self):
        return self._xp

    def inc_xp(self, amount):
        self._xp += amount
        if self._xp >= self._max_hp:
            self.level_up()

    def get_inventory(self):
        return self._inventory

    def check_inventory(self, item):
        return item in self._inventory

    def remove_item(self, item):
        self._inventory.remove(item)

    def receive_loot(self, items):
        self._inventory.extend(items)

    def prompt_action(self):
        print('What will you do?')
        print('fight, flight, advance, loot, or item')
        print_break()
        action = input()
        return action

    def prompt_item_action(self, monster, phase):
            while True:
                print('Which item would you like to use?')
                print(f'{self.get_inventory()}')
                print(f'or type back')
                print_break()
                item_action = input()
                if self.check_inventory(item_action):
                    if (phase == 'fight' or 
                        (phase == 'not_fight' and 
                         item_action.startswith('Potion'))):
                        self.remove_item(item_action)
                        use_item(self, monster, item_action)
                        print_break()
                        return True
                    else:
                        print('Only potion items can be used out of combat.')
                elif item_action == 'back':
                    if phase == 'fight':
                        self.fight(monster)
                        return False
                    else:
                        return True
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
            print(f'A {monster.get_name()} now lies before you.')
        if not self.is_alive():
            print(f'You have been slain by {monster.get_name()}!')
        print_break()

    def fight(self, monster):
        engaged = False
        while self.is_alive() and monster.is_alive():
            engaged = True
            print('Choose your action:')
            print('attack, item, flee')
            print_break()
            fight_action = input()
            if fight_action == 'attack':
                damage = self.get_attack() - monster.get_defense()
                if damage < 0:
                    damage = 0
                monster.dec_hp(damage)
                print(f'You attack dealing {damage} damage!')
                if monster.is_alive():
                    print(f'{monster.get_name()} now has {monster.get_hp()} hitpoints')
                print_break()
            elif fight_action == 'item':
                if not self.prompt_item_action(monster, 'fight'):
                    break
            elif fight_action == 'flee':
                return False
            if monster.is_alive():
                damage = monster.get_attack() - self.get_defense()
                if damage < 0:
                    damage = 0
                print(f'{monster.get_name()} attacks you for {damage} damage!')
                self.dec_hp(damage)
                if self.is_alive():
                    print(f'You have {self.get_hp()} hp remaining!')
                    print_break()

        if not monster.is_alive() and engaged:
            print(f'You have slain a monster!')
            print(f'A {monster.get_name()} now lies before you.')
        if not self.is_alive():
            print(f'You have been slain by {monster.get_name()}!')
        print_break()
        return True
