from random import randint
from colorama import *


def to_hit(args):
    weapon_range = float(args[1])
    distance = float(args[2])
    ratio = weapon_range / distance
    if ratio >= weapon_range / 2:
        return "Point Blank, 10 to hit, max damage"
    elif ratio >= 4:
        return "Close, 15 to hit"
    elif ratio >= 2:
        return "Medium, 20 to hit"
    elif ratio >= 1:
        return "Long, 25 to hit"
    else:
        return "Extreme, 30 to hit"


def roll(args):
    try:
        num_dice = int(args[1].split("d")[0])
    except ValueError:
        num_dice = 1

    try:
        dice_type = int(args[1].split("d")[1])
    except ValueError:
        return Fore.RED + "INVALID ARGS" + Fore.LIGHTRED_EX
    if dice_type == 0:
        return Fore.RED + "INVALID ARGS" + Fore.LIGHTRED_EX

    dice_roll = 0
    for i in range(num_dice):
        dice_roll += randint(1, dice_type)
    return str(dice_roll)


def help_function(args):
    cmd_arr = ["to_hit", "search_weapons", "weapon_desc_format", "search_cybernetics", "cybernetics_desc_format",
               "roll", "generate_char"]
    help_dict = {
        "to_hit": "Calculates hit difficulty.\n" + "to_hit [weapon_range] [target_distance]",
        "search_weapons": "Searches through the weapon index.\n" + "search_weapons [keyword]",
        "weapon_desc_format": "Displays weapon format.",
        "search_cybernetics": "Searches through the cybernetics index.\n" + "search_cybernetics [keyword]",
        "cybernetics_desc_format": "Displays cybernetics format.",
        "roll": "Rolls dice.\n" + "roll [number of dice]d[number of sides]",
        "generate_char": "Randomly generates a character."
    }
    try:
        return help_dict[args[1]]
    except IndexError:
        return '\n'.join(cmd_arr)


print("Imported quick_functions...")
print("Imported help...")
