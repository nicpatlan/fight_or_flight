import random
from player import Player
from monster import generate_monster
from room import Room
from items import generate_item, generate_gold

def print_break():
    print('============================================================')
    print('')

class Tower():
    def __init__(self, name):
        self._rooms = []
        self._room_idx = 0
        self._player = Player(name, 1, 10, 2, 1)

        # give player some random items
        start_items = []
        for i in range(3):
            random_val = random.randrange(6)
            start_items.append(generate_item(random_val))
        self._player.receive_loot(start_items)
        
        # add the first room and enter
        self._generate_room()
        self._player_enter_room()

    def _generate_room(self):
        # add room to tower list of rooms
        random_val = random.randrange(6)
        room_loot = [generate_item(random_val)]
        level = self._player.get_level()
        monster_loot = [generate_gold() for i in range(level)]
        rarity = random.randrange(100)
        if rarity > 89:
            for i in range(2):
                monster_loot.append(generate_item(rarity % 6))
                random_val = random.randrange(2, 6)
        elif rarity > 75:
            monster_loot.append(generate_item(rarity % 6))
            random_val = random.randrange(1, 5)
        else:
            random_val = random.randrange(4)
        room_monster = generate_monster(random_val, level, monster_loot) 
        self._rooms.append(Room(room_monster, room_loot))

    def prompt_action(self):
        print('What will you do?')
        print('fight, flight, advance, loot, item, or status')
        print_break()
        action = input()
        return action

    def prompt_item_action(self, player, monster):
            while True:
                print('Which item would you like to use?')
                print(f'{player.get_inventory()}')
                print(f'or type back')
                print_break()
                item_action = input()
                if player.check_inventory(item_action) >= 0:
                    item = player.remove_item(item_action)
                    item.use_item(player, monster)
                    print_break()
                    return True
                elif item_action == 'back':
                    return False
                else:
                    print('You do not have that item.')

    def fight_round(self, player, monster, item=False):
        if not item:
            damage = player.get_attack() - monster.get_defense()
            if damage < 0:
                damage = 0
            monster.dec_hp(damage)
            print(f'You attack dealing {damage} damage!')
            if monster.is_alive():
                print(f'{monster.get_name()} now has {monster.get_hp()} hitpoints')
            print_break()
        if monster.is_alive():
            damage = monster.get_attack() - player.get_defense()
            if damage < 0:
                damage = 0
            print(f'{monster.get_name()} attacks you for {damage} damage!')
            player.dec_hp(damage)
            if player.is_alive():
                print(f'You have {player.get_hp()} hp remaining!')
                print_break()
        else:
            print(f'You have slain a monster!')
            xp = monster.get_xp_gain()
            player.inc_xp(xp)
            print(f'A {monster.get_name()} now lies before you.')
            print_break()
        if not player.is_alive():
            print(f'You have been slain by a {monster.get_name()}!')
            print_break()
    
    def _player_enter_room(self):
        # describe the room and its contents
        self._rooms[self._room_idx].description()
        moved = False

        # as long as the player is in the current room
        while not moved and self._player.is_alive():
            action = self.prompt_action()
            # no searching if a monster is present
            if action == 'loot' and self._rooms[self._room_idx].get_occupied():
                print(f'The {self._rooms[self._room_idx].get_monster().get_name()} moves to engage.')
                action = 'fight'
            # respond to player action
            if action == 'fight':
                if not self._rooms[self._room_idx].get_occupied():
                    print(f'There is no monster to fight.')
                    print_break()
                    continue
                # monster and player fight
                self.fight_round(self._player, self._rooms[self._room_idx].get_monster())
            elif action == 'loot':
                loot = self._rooms[self._room_idx].get_loot()
                print(f'You find {loot} in the room.')
                print_break()
                self._player.receive_loot(loot)
            elif action == 'flight' or action == 'advance':
                moved = True
            elif action == 'item':
                if not self.prompt_item_action(self._player, self._rooms[self._room_idx].get_monster()):
                    continue
                if self._rooms[self._room_idx].get_occupied():
                    self.fight_round(self._player, self._rooms[self._room_idx].get_monster(), True)
            elif action == 'status':
                self._player.status()
                print_break()
            if not self._rooms[self._room_idx].get_monster().is_alive():
                self._rooms[self._room_idx].set_not_occupied()

        if action == 'flight':
            self._room_idx -= 1
            if self._room_idx < 0:
                self._room_idx = 0
        elif action == 'advance':
            self._room_idx += 1
            if len(self._rooms) == self._room_idx:
                self._generate_room()
        if self._player.is_alive():
            self._player_enter_room()
        else:
            print('Game Over: how much gold did you get?')
