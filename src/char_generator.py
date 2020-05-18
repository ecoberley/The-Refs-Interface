from random import randint, sample, choice
from math import trunc

stats_dict = {
    "INT": 0,
    "REF": 0,
    "TECH": 0,
    "COOL": 0,
    "ATTR": 0,
    "LUCK": 0,
    "MA": 0,
    "BODY": 0,
    "EMP": 0
}

classes_dict = {
    "Solo": {
        "Combat Sense": 0,
        "Notice": 0,
        "Handgun": 0,
        "Brawling": 0,
        "Melee": 0,
        "Weapons Tech": 0,
        "Rifle": 0,
        "Athletics": 0,
        "Submachinegun": 0,
        "Stealth": 0
    },

    "Rocker": {
        "Charismatic Leadership": 0,
        "Notice": 0,
        "Perform": 0,
        "Wardrobe & Style": 0,
        "Composition": 0,
        "Brawling": 0,
        "Play Instrument": 0,
        "Streetwise": 0,
        "Persuasion": 0,
        "Seduction": 0
    },

    "Netrunner": {
        "Interface": 0,
        "Notice": 0,
        "Basic Tech": 0,
        "Education": 0,
        "System Knowledge": 0,
        "CyberTech": 0,
        "Cyberdeck Design": 0,
        "Composition": 0,
        "Electronics": 0,
        "Programming": 0
    },

    "Media": {
        "Credibility": 0,
        "Notice": 0,
        "Composition": 0,
        "Education": 0,
        "Persuasion": 0,
        "Human Perception": 0,
        "Social": 0,
        "Streetwise": 0,
        "Photo & Film": 0,
        "Interview": 0
    },

    "Nomad": {
        "Family": 0,
        "Notice": 0,
        "Endurance": 0,
        "Melee": 0,
        "Rifle": 0,
        "Drive": 0,
        "Basic Tech": 0,
        "Wilderness Survival": 0,
        "Brawling": 0,
        "Athletics": 0
    },

    "Fixer": {
        "Streetdeal": 0,
        "Notice": 0,
        "Forgery": 0,
        "Handgun": 0,
        "Brawling": 0,
        "Melee": 0,
        "Pick Lock": 0,
        "Pick Pocket": 0,
        "Intimidate": 0,
        "Persuasion": 0,
    },

    "Cop": {
        "Authority": 0,
        "Notce": 0,
        "Handgun": 0,
        "Human Perception": 0,
        "Athletics": 0,
        "Education": 0,
        "Brawling": 0,
        "Melee": 0,
        "interrogation": 0,
        "Streetwise": 0
    },

    "Corp": {
        "Resources": 0,
        "Notice": 0,
        "Human Perception": 0,
        "Education": 0,
        "Library Search": 0,
        "Social": 0,
        "Persuasion": 0,
        "Stock Market": 0,
        "Wardrobe & Style": 0,
        "Personal Grooming": 0
    },

    "Techie": {
        "Jury Rig": 0,
        "Notice": 0,
        "Basic Tech": 0,
        "CyberTech": 0,
        "Teaching": 0,
        "Education": 0,
        "Electronics": 0,
        "Gyro": 0,
        "Aero": 0,
        "Weapons": 0
    },

    "Medtechie": {
        "Medical Tech": 0,
        "Notice": 0,
        "Basic Tech": 0,
        "Diagnose": 0,
        "Education": 0,
        "Cyotank Operation": 0,
        "Library Search": 0,
        "Pharmaceuticals": 0,
        "Zoology": 0,
        "Human Perception": 0
    }

}

cyberware = {
    1: {  # Cyberoptics
        1: "Cyberoptics - Infrared",
        2: "Cyberoptics - Lowlight",
        3: "Cyberoptics - Camera",
        4: "Cyberoptics - Dartgun",
        5: "Cyberoptics - Antidazzle",
        6: "Cyberoptics - Targeted scope"
    },

    2: {  # Cyberarm with gun
        1: "Cyberarm with Med. Pistol",
        2: "Cyberarm with Light Pistol",
        3: "Cyberarm with Med. Pistol",
        4: "Cyberarm with Light Submachinegun",
        5: "Cyberarm with Very Heavy Pistol",
        6: "Cyberarm with Heavy Pistol"
    },

    3: {  # Cyberaudio
        1: "Cyberaudio - Wearman",
        2: "Cyberaudio - Radio Splice",
        3: "Cyberaudio - Phone Link",
        4: "Cyberaudio - Amplified Hearing",
        5: "Cyberaudio - Sound Editing",
        6: "Cyberaudio - Digital Recording Link"
    },

    4: "Big Knucks",

    5: "Rippers",

    6: "Vampires",

    7: "Slice n'dice",

    8: "Reflex Boost (Kerenzikov)",

    9: "Reflex Boost (Sandevistan)",

    10: None
}

sp = {
    "Head": 0,
    "Arms": 0,
    "Torso": 0,
    "Legs": 0
}

armour = {
    1: "Heavy Leather",
    2: "ArmorVest",
    3: "Light Armor jacket",
    4: "Light Armor jacket",
    5: "Med Armor jacket",
    6: "Med. Armor jacket",
    7: "Med. Armor jacket",
    8: "Hvy. Armor jacket",
    9: "Hvy. Armor jacket",
    10: "MetalGear"
}

weapons = {
    1: "Knife",
    2: "Light Pistol",
    3: "Medium Pistol",
    4: "Heavy Pistol",
    5: "Heavy Pistol",
    6: "Light SMG",
    7: "Lt. Assault Rifle",
    8: "Med. Assault Rifle",
    9: "Hvy. Assault Rifle",
    10: "Hvy. Assault Rifle"
}


# This just runs through the values in stats_dict and assigns them a random int between 1 and 8 and adds 2.
# It makes sure the numbers are never 1 or 2, since your always adding 2, and it never goes over 10 since
# the highest number it can generate is 8+2.
def assign_stats():
    for x in stats_dict:
        stats_dict[x] = randint(1, 8) + 2

    stats_dict["Run"] = stats_dict["MA"] * 9
    stats_dict["Leap"] = int(trunc(stats_dict["Run"] / 4))
    stats_dict["Lift"] = stats_dict["BODY"] * 10


# Will generate n amount of numbers which will add up to the total.
# Not entirely sure how it works, but it works.
# Gonna use it generate random values for different skills.
def constrained_sum_sample_pos(n, total):
    dividers = sorted(sample(range(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]


# This is meant to assign the different array items to the different skills according to char_class.
# But, I have no idea how to do that. I've tried everything I could at the  moment but nothing seems to work.
# I may have just made things really complicated for myself since I used a nested dictionary but I dunno.
def assign_career_skills():
    skill_spread = constrained_sum_sample_pos(10, 40)

    print(skill_spread)


# This is meant to assign possessions to the character. I've got it mostly working. Only hiccup is that you're meant
# to re-roll if you roll for the same possession, and I'm not really sure how to do that without making the code
# less awkward than it already is.
def assign_possessions():
    possessions = []

    for i in range(3):
        possession_num1 = randint(1, 10)

        if possession_num1 > 3:
            possessions.append(cyberware[possession_num1])

        else:
            possession_num2 = randint(1, 6)

            possessions.append(cyberware[possession_num1][possession_num2])

    return possessions


# Assigns the character armour and weapons. Not really sure how to apply appropriate SP though.
def assign_armour_and_weapons(char_class):
    modifier = 3
    char_armour = ""
    char_weapon = ""

    if char_class == "Nomad" or "Cop":
        modifier == 2
    elif char_class == "Solo":
        modifier == 3
    else:
        modifier == 0

    try:
        assigning_num_armour = (randint(1, 10))

        char_armour = armour[assigning_num_armour + modifier]
    except KeyError:
        char_armour = armour[10]

    try:
        assigning_num_weapons = randint(1, 10)

        char_weapon = weapons[assigning_num_weapons + modifier]
    except KeyError:
        char_weapon = weapons[10]

    return char_weapon, char_armour


# This is what is run at the end. I know it's really clunky, but this is just kinda the base idea of what I think
# this should be.
def generate_char(args):
    stats_text = "Stats:\n"
    possessions_text = "Possessions:\n"
    char_possessions = []

    char_class = choice(list(classes_dict.keys()))
    assign_stats()
    char_possessions += assign_possessions()
    char_possessions += assign_armour_and_weapons(char_class)

    for x, y in stats_dict.items():
        stats_text += "{}: {}\n".format(x, y)

    for i in char_possessions:
        possessions_text += "{}\n".format(i)

    final_text = "{}\n\n{}\n\n{}".format(char_class, stats_text, possessions_text)

    return final_text


# Maybe if fantasy name generator has an API we could add it to here and have it generate names depending on class.
# As I said earlier, I know this is very clunky so far but this is just a kinda base script from which we can
# work from.
