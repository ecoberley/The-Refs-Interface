class Weapon:
    name = ""
    type = ""
    accuracy = ""
    concealability = ""
    availability = ""
    damage_ammo = ""
    num_shots = ""
    rof = ""
    reliability = ""
    range = ""
    cost = ""

    def __init__(self, row):
        self.desc = ""
        self.name = str(row[0])
        self.type = str(row[1])
        self.accuracy = str(row[2])
        self.concealability = str(row[3])
        self.availability = str(row[4])
        self.damage_ammo = str(row[5])
        self.num_shots = str(row[6])
        self.rof = str(row[7])
        self.reliability = str(row[8])
        self.range = str(row[9])
        self.cost = str(row[10])

    def to_string(self):
        string = ""
        string += self.name + " • "
        string += self.type + " • "
        string += self.accuracy + " • "
        string += self.concealability + " • "
        string += self.availability + " • "
        string += self.damage_ammo + " • "
        string += self.num_shots + " • "
        string += self.rof + " • "
        string += self.reliability + " • "
        string += self.range + " • "
        string += self.cost

        return string
