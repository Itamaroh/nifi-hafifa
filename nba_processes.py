import subprocess
import os

NAME_PATH = r'C:\Users\itamar\{}.exe'

allStar_players = ["lebron","kevin","kobe","steph"]
old_name = "process"

for player in allStar_players:
    os.rename(NAME_PATH.format(old_name),NAME_PATH.format(player))
    subprocess.Popen(NAME_PATH.format(player))
    old_name = player
os.rename(NAME_PATH.format(old_name),NAME_PATH.format("process"))


