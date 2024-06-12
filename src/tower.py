from player import Player
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
        self._rooms.append(Room(Monster('a kobold', 1, 3, 1, 1)))

    def _player_enter_room(self):
        # describe the room and its contents
        cur_room = self._rooms[self._room_idx]
        cur_room.description()
        moved = False

        # as long as the player is in the current room
        while not moved and self._player.is_alive():
            action = self._player.prompt_action()

            # no searching if a monster is present
            if action == 'loot' and cur_room.get_occupied():
                action = 'fight'

            # respond to player action
            if action == 'fight':
                # monster and player fight
                if not self._player.fight(cur_room.get_monster()):
                    break
                if not cur_room.get_monster().is_alive():
                    cur_room.set_not_occupied()
            elif action == 'loot':
                loot = cur_room.get_loot()
                self._player.receive_loot(loot)
            elif action == 'flight' or action == 'advance':
                moved = True
            elif action == 'bag':
                print(self._player.get_inventory())

        if action == 'flight':
            self._room_idx -= 1
        elif action == 'advance':
            self._room_idx += 1
            if len(self._rooms) == self._room_idx:
                self._generate_room()
        if self._player.is_alive():
            self._player_enter_room()
        else:
            print('Game Over: how much gold did you get?')
