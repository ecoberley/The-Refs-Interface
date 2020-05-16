
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


print("Imported quick_functions...")
