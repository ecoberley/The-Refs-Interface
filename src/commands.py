from quick_functions import *
from weapons import *
from cybernetics import *
from char_generator import *

cmd_dict = {
    # Finds the hit difficulty of a given shot from
    # the weapon range and distance from the target
    "to_hit": to_hit,
    "search_weapons": search_weapons,
    "weapon_desc_format": weapon_desc_format,
    "search_cybernetics": search_cybernetics,
    "cybernetic_desc_format": cybernetic_desc_format,
    "roll": roll,
    "help": help_function,

}
