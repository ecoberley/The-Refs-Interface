from startup import *
from commands import *
from colors import *


cmd = ""
while cmd.lower() != "exit":
    try:
        args = input("\nC:\\IMI\\interface>").lower().split(" ")
        cmd = args[0]
        if cmd == "exit":
            break
        print(cmd_dict[cmd](args))
    except KeyError:
        print(bcolors.FAIL + "INVALID COMMAND" + bcolors.GREEN)
    except IndexError:
        print(bcolors.FAIL + "INVALID ARGS" + bcolors.GREEN)
