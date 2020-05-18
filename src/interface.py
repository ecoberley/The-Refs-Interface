from colorama import *
from random import uniform
from time import sleep
from startup import *
init()
IMI_logo_split = IMI_logo.split("\n")
for i in IMI_logo_split:
    sleep(uniform(0.2, 0.29))
    print(Fore.LIGHTRED_EX + i)
from commands import *


cmd = ""
while cmd.lower() != "exit":
    try:
        args = input("\nC:\\IMI\\interface>").lower().split(" ")
        cmd = args[0]
        if cmd == "exit":
            break
        print(cmd_dict[cmd](args))
    except KeyError:
        print(Fore.RED + "INVALID COMMAND" + Fore.LIGHTRED_EX)
    except IndexError:
        print(Fore.RED + "INVALID ARGS" + Fore.LIGHTRED_EX)

# TODO Compile V1.1.04
