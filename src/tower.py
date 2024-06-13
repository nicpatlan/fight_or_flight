from player import Player, print_break
from monster import Monster
from room import Room

class Tower():
    def __init__(self, name):
        self._rooms = []
        self._room_idx = 0
        self._player = Player(name, 1, 10, 2, 2)
        
        # add the first room and enter
        self._generate_room()
        self._player_enter_room()

    def _generate_room(self):
        # add room to tower list of rooms
        self._rooms.append(Room(Monster('kobold', 1, 3, 5, 1)))

    def _player_enter_room(self):
        # describe the room and its contents
        self._rooms[self._room_idx].description()
        moved = False

        # as long as the player is in the current room
        while not moved and self._player.is_alive():
            action = self._player.prompt_action()
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
                if not self._player.fight(self._rooms[self._room_idx].get_monster()):
                    break
                if not self._rooms[self._room_idx].get_monster().is_alive():
                    self._rooms[self._room_idx].set_not_occupied()
            elif action == 'loot':
                loot = self._rooms[self._room_idx].get_loot()
                print(f'You find {loot} in the room.')
                print_break()
                self._player.receive_loot(loot)
            elif action == 'flight' or action == 'advance':
                moved = True
            elif action == 'bag':
                print(self._player.get_inventory())
                print_break()

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
