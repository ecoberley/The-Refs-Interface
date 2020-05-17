from random import uniform
from time import sleep
from src.colors import *
# from subprocess import Popen

# p = Popen("start.bat", cwd=r"D:\Python\The-Refs-Interface-master\src")

# stdout, stderr = p.communicate()

IMI_logo = bcolors.GREEN + \
           "*************************************************\n" \
           "****** WELCOME TO THE REFEREE'S INTERFACE© ******\n" \
           "************ BROUGHT TO YOU BY IMI™ *************\n" \
           "*************************************************\n" \
           "███████████  ████████       ████████  ███████████\n" \
           "███████████  █████████     █████████  ███████████\n" \
           "   █████       ████████   ████████       █████   \n" \
           "   █████       ████  ███ ███  ████       █████   \n" \
           "   █████       ████  ███████  ████       █████   \n" \
           "   █████       ████   █████   ████       █████ © \n" \
           "███████████  ██████    ███    ██████  ███████████\n" \
           "███████████  ██████     █     ██████  ███████████\n" \
           "*************************************************\n" \
           "*   This system  is for the use of authorized   *\n" \
           "*  users only. Usage of this interface will be  *\n" \
           "*            monitored and recorded             *\n" \
           "*************************************************\n" \

IMI_logo_split = IMI_logo.split("\n")

for i in IMI_logo_split:
    sleep(uniform(0.2, 0.29))
    print(i)
