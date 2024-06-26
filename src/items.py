ITEM_LIST = ['Potion of Healing',
             'Potion of Attack',
             'Potion of Defense',
             'Fireball Scroll',
             'Shrink Scroll',
             'Experience Scroll']

def generate_item(random_val):
    return Item(ITEM_LIST[random_val])

def generate_gold():
    return Item('Gold')

class Item():
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def use_item(self, player, monster):
        if self._name == ITEM_LIST[0]:
            amount = player.get_level() * 3
            player.inc_hp(amount)
            print(f'You gain {amount} hp.')
            print(f'You have {player.get_hp()} hp.')
        elif self._name == ITEM_LIST[1]:
            amount = (player.get_level() + 1) // 2
            player.inc_attack(amount)
            print(f'You gain {amount} attack.')
            print(f'You have {player.get_attack()} attack.')
        elif self._name == ITEM_LIST[2]:
            amount = (player.get_level() + 1) // 2
            player.inc_defense(amount)
            print(f'You gain {amount} defense.')
            print(f'You have {player.get_defense()} defense.')
        elif self._name == ITEM_LIST[3]:
            amount = player.get_level() * 4
            monster.dec_hp(amount) 
            print(f'Fireball deals {amount} damage.')
            if monster.is_alive():
                print(f'The {monster.get_name()} has {monster.get_hp()} hp.')
        elif self._name == ITEM_LIST[4]:
            amount = (player.get_level() + 1) // 2
            monster.dec_attack(amount)
            monster.dec_defense(amount)
            print(f'The {monster.get_name()}s shrinks before your eyes!')
            print(f'{monster.get_name()} attack decreased by {amount}.')
            print(f'{monster.get_name()} defense decreased by {amount}.')
        elif self._name == ITEM_LIST[5]:
            amount = player.get_level() * 2
            player.inc_xp(amount)

    def __repr__(self):
        return self._name
