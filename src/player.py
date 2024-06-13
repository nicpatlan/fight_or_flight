from entity import Entity

def print_break():
    print('=============================================')
    print('')

class Player(Entity):
    def __init__(self, name, level, hp, attack, defense):
        super().__init__(name, level, hp, attack, defense)
        self._inventory = ['Stick', 'Potion', 'Scroll']

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
        print('fight, flight, advance, loot, or bag')
        print_break()
        action = input()
        return action

    def fight(self, monster):
        engaged = False
        while self.is_alive() and monster.is_alive():
            engaged = True
            print('Choose your action:')
            print('attack, item, run')
            print_break()
            fight_action = input()
            if fight_action == 'attack':
                damage = self.get_attack() - monster.get_defense()
                if damage < 0:
                    damage = 0
                monster.dec_hp(damage)
                print(f'You attack dealing {damage} damage!')
                print(f'{monster.get_name()} now has {monster.get_hp()} hitpoints')
                print_break()
            elif fight_action == 'item':
                resolved = False
                while not resolved:
                    print('Which item would you like to use:')
                    print(f'{self.get_inventory()}')
                    print_break()
                    item_action = input()
                    if self.check_inventory(item_action):
                        resolved = True
                        self.remove_item(item_action)
                        print(f'Using {item_action}')
                        print_break()
            elif fight_action == 'run':
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
