ITEM_LIST = ['Potion of Healing',
             'Potion of Attack',
             'Potion of Defense',
             'Fireball Scroll',
             'Shrink Scroll',
             'Experience Scroll']

def use_item(player, monster, item):
    if item == ITEM_LIST[0]:
        amount = player.get_level() * 3
        player.inc_hp(amount)
        print(f'You gain {amount} hp.')
        print(f'You have {player.get_hp()} hp.')
    elif item == ITEM_LIST[1]:
        amount = player.get_level()
        player.inc_attack(amount)
        print(f'You gain {amount} attack.')
        print(f'You have {player.get_attack()} attack.')
    elif item == ITEM_LIST[2]:
        amount = player.get_level()
        player.inc_defense(amount)
        print(f'You gain {amount} defense.')
        print(f'You have {player.get_defense()} defense.')
    elif item == ITEM_LIST[3]:
        amount = player.get_level() * 4
        monster.dec_hp(amount) 
        print(f'Fireball deals {amount} damage.')
        if monster.is_alive():
            print(f'The {monster.get_name()} has {monster.get_hp()} hp.')
    elif item == ITEM_LIST[4]:
        amount = player.get_level()
        monster.dec_attack(amount)
        monster.dec_defense(amount)
        print(f'{monster.get_name()} shrinks before your eyes!')
        print(f'{monster.get_name()} attack decreases by {amount}.')
        print(f'{monster.get_name()} defense decreases by {amount}.')
    elif item == ITEM_LIST[5]:
        amount = player.get_level() * 2
        player.inc_xp(amount)
        print(f'You gain {amount} xp. You have {player.get_xp()} total xp.')
