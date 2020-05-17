cmd_arr = ["to_hit", "search_weapons", "weapon_desc_format", "search_cybernetics", "cybernetics_desc_format", "roll"]


def help_function(args):
    if args[1] == "":
        return "\n".join(cmd_arr)

    elif args[1] == cmd_arr[0]:
        return "Determines amount needed to hit.\n" \
                "to_hit [weapon range] [target distance]"

    elif args[1] == cmd_arr[1]:
        return "Searches through the weapon index.\n" \
                "search_weapons [search terms]"

    elif args[1] == cmd_arr[2]:
        return "Displays weapon format."

    elif args[1] == cmd_arr[3]:
        return "Searched through the cybernetics index.\n" \
                "search_cybernetics [search terms]"

    elif args[1] == cmd_arr[4]:
        return "Displays cybernetics format."

    elif args[1] == cmd_arr[5]:
        return "Rolls dice.\n" \
                "roll d[number of sides]"
