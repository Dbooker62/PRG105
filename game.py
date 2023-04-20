class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.friendly = False
        self.type_of_creature = "Creature"

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_level(self):
        return self.level

    def set_level(self, level):
        self.level = level

    def get_friendly(self):
        return self.friendly

    def set_friendly(self, friendly):
        self.friendly = friendly

    def get_type_of_creature(self):
        return self.type_of_creature

    def set_type_of_creature(self, type_of_creature):
        self.type_of_creature = type_of_creature

    def __str__(self):
        return f"{self.name} ({self.type_of_creature}), Level: {self.level}, Friendly: {self.friendly}"


class Orc(Creature):
    def __init__(self, name, level, weapon, max_hit_points, current_hit_points):
        super().__init__(name, level)
        self.weapon = weapon
        self.max_hit_points = max_hit_points
        self.current_hit_points = current_hit_points
        self.type_of_creature = "Orc"
        self.friendly = False

    def get_weapon(self):
        return self.weapon

    def set_weapon(self, weapon):
        self.weapon = weapon

    def get_max_hit_points(self):
        return self.max_hit_points

    def set_max_hit_points(self, max_hit_points):
        self.max_hit_points = max_hit_points

    def get_current_hit_points(self):
        return self.current_hit_points

    def set_current_hit_points(self, current_hit_points):
        self.current_hit_points = current_hit_points

    def __str__(self):
        return f"{super().__str__()}, Weapon: {self.weapon}, Max Hit Points: {self.max_hit_points}, Current Hit Points: {self.current_hit_points}"


class OrcBoss(Orc):
    def __init__(self, name, level, weapon, max_hit_points, current_hit_points, special_move):
        super().__init__(name, level, weapon, max_hit_points, current_hit_points)
        self.special_move = special_move

    def get_special_move(self):
        return self.special_move

    def set_special_move(self, special_move):
        self.special_move = special_move

    def __str__(self):
        return f"{super().__str__()}, Special Move: {self.special_move}"


if __name__ == "__main__":
    c = Creature("Creature", 1)
    print(c)

    o = Orc("Orc", 2, "Sword", 10, 8)
    print(o)

    ob = OrcBoss("Orc Boss", 3, "Axe", 20, 18, "Thunder Strike")
    print(ob)
