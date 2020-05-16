class Cybernetic:
    name = ""
    surgery_type = ""
    cost = ""
    humanity_loss = ""
    availability = ""
    desc = ""

    def __init__(self, row):
        self.name = str(row[0])
        self.surgery_type = str(row[1])
        self.cost = str(row[2])
        self.humanity_loss = str(row[3])
        self.availability = str(row[4])
        self.desc = str(row[5])

    def to_string(self):
        string = ""
        string += self.name + " • "
        string += self.surgery_type + " • "
        string += self.cost + " • "
        string += self.humanity_loss + " • "
        string += self.availability + " • "
        string += self.desc

        return string
