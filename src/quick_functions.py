from random import randint
from colors import *


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
        dice_roll = 0
    except ValueError:
        return bcolors.FAIL + "INVALID ARGS" + bcolors.GREEN

    for i in range(num_dice):
        dice_roll += randint(1, dice_type)
    return str(dice_roll)


print("Imported quick_functions...")
