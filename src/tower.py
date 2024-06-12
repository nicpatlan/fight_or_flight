class Tower():
    def __init__(self, name):
        self._rooms = []
        self._room_idx = 0
        self._player = Player(name)
        
        # add the first room and enter
        self._generate_room()
        self._player_enter_room()

    def _generate_room(self):
        # add room to tower list of rooms
        self._rooms.append(Room())

    def _player_enter_room(self):
        # describe the room and its contents
        cur_room = self._rooms[self._room_idx]
        cur_room.description()
        moved = False

        # as long as the player is in the current room
        while moved == False:
            action = self._player.prompt_action()

            # no searching if a monster is present
            if action == "loot" and cur_room.get_occupied():
                action = "fight"

            # respond to player action
            if action == "fight":
                # monster and player fight
                player.fight(cur_room.get_monster())
            elif action == "loot":
                loot = cur_room.get_loot()
                player.receive_loot(loot)
            elif action == "flight" or action == "advance":
                moved = True

        if action == "flight":
            self._room_idx -= 1
        elif action = "advance":
            self._room_idx += 1
            if len(self._rooms) == self._room_idx:
                self._generate_room()
        self._player_enter_room()
