# The Referee's Interface

## This project, in its current form, has been abandoned. 
It wasn't implemented nearly as well as it could have been, and I used it mostly as a quick test of my knowledge of Python.
As I learn more data structures and play around with SQL, I'm working on an updated, cleaner version of the project that will most likely be released under a different name. 
However, I will leave the repo up for the time being, since some people have found the project useful ( and as a humbling reminder of how little I used to know about software development ).

## How to download
Click **clone or download** in the top-right hand corner and download as ZIP. **Extract** the ZIP anywhere you'd like.
The only files you technically need are in the RefsInterface folder, including the executable and the workbook for the weapons and cybernetics lists, so you can add entries to them if you'd like.
However, I've included the source code if you're familiar with Python and would
like to change anything and compile your own executable.

## Windows Defender will likely tell you it's not safe
I'm not experienced enough to code any sort of cryptominer, keystroke logger,
or anything else that you should be scared about. It won't make changes to 
your hard drive either. If you're wary, check the source code, it gets pushed
when the executable does.

## Legal (?)
This program is for personal use only. I'm a college student. If you're going
to sell it, at least cut me in. **All copyright, trademark, and registered**
**symbols are purely aesthetic.** IMI is a fictional company, and the user
warning shown on startup is just for show. I do not claim to have copyright
on any of the logos and IPs shown in the program.

## How to use
After startup is finished, you'll be shown a command prompt. These are the available commands.

**to_hit [weapon_range] [distance_from]**
Input the range of the weapon and the distance from the target, i.e. to_hit 300 150

**search_weapons [keyword]**
Input the keyword you'd like to be searched, i.e. search_weapons arasaka.
The weapons list includes any and all weapons found on the Cyberpunk 2020 wiki.
In addition, the search returns a result if the keyword is present *anywhere* in the
weapons description. If you say search_weapons 60 to find a range of 60, you will
get back weapons that have a range of 60, but also a price of 60 or 600.

**search_cybernetics [keyword]**
Like search_weapons, but with cybernetics. List taken from https://silcyberclassic.neocities.org/silcyber.htm. Doesn't include cybernetics from sourcebooks outside of the Player's Handbook, but entries can be added in the cybernetics_list.xlsx spreadsheet.

**weapon_desc_format**
Outputs the standard format that Cyberpunk weapons are written in.

**cybernetic_desc_format**
Outputs the standard format that Cyberpunk cybernetics are written in.

**roll [num_dice]d[num_sides]**
Input the number of a specific type of dice, i.e. roll 2d10.
If you're rolling 1dx, you can omit the number of dice, i.e. roll d6.

**help [cmd]**
Input the command you'd like help with, i.e. help to_hit.
  
**help**
Outputs a list of useable commands.

**For questions, comments, or suggestions, email me at ecoberley@outlook.com**
