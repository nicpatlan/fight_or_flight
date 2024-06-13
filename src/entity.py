class Entity():
    def __init__(self, name, level, hp, attack, defense):
        self._name = name
        self._level = level
        self._max_hp = hp
        self._hp = hp
        self._attack = attack
        self._defense = defense
        self._alive = True

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def get_max_hp(self):
        return self._max_hp

    def inc_max_hp(self, amount):
        self._max_hp += amount

    def dec_max_hp(self, amount):
        self._max_hp -= amount
        if self._hp > self._max_hp:
            self._hp = self._max_hp

    def get_hp(self):
        return self._hp

    def inc_hp(self, amount):
        self._hp += amount
        if self._hp > self._max_hp:
            self._hp = self._max_hp

    def dec_hp(self, amount):
        self._hp -= amount
        if self._hp < 1:
            self._alive = False
            old_name = self._name
            self._name = f'dead {old_name}' 

    def get_attack(self):
        return self._attack

    def inc_attack(self, amount):
        self._attack += amount

    def dec_attack(self, amount):
        self._attack -= attack
        if self._attack < 1:
            self._attack = 1

    def get_defense(self):
        return self._defense

    def inc_defense(self, amount):
        self._defense += amount

    def dec_defense(self, amount):
        self._defense -= amount
        if self._defense < 0:
            self._defense = 0

    def is_alive(self):
        return self._alive
