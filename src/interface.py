import src.startup
from src.commands import cmd_dict

cmd = ""
while cmd.lower() != "exit":
    try:
        args = input("\nC:\\IMI\\interface>").lower().split(" ")
        cmd = args[0]
        if cmd == "exit":
            break
        print(cmd_dict[cmd](args))
    except KeyError:
        print("INVALID COMMAND")
    except IndexError:
        print("INVALID ARGS")


