import xlrd
from src.weapon import *

filename = "weapons_list.xlsx"
weapons_spreadsheet = xlrd.open_workbook(filename).sheet_by_index(0)

weapons = []
for i in range(1, weapons_spreadsheet.nrows):
    temp_weapon = Weapon(weapons_spreadsheet.row_values(i))
    weapons.append(temp_weapon)
print("Imported weapons_list...")


def search_weapons(args):
    results = weapon_desc_format(0)
    query = args[1].lower()
    for idx in range(0, len(weapons)):
        if weapons[idx].to_string().lower().__contains__(query):
            if idx != len(weapons) - 1:
                results += weapons[idx].to_string() + "\n"
            else:
                results += weapons[idx].to_string()
    if results == weapon_desc_format(0):
        return "No results found"
    else:
        return results


def weapon_desc_format(args):
    return "[Name • Type • Accuracy • Concealability •  Availability • Damage/Ammo • #Shots • RoF • Reliability • " \
           "Range • Cost]\n"
