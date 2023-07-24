PAUSE_DURATION = 3
MONSTERS_PER_FLOOR = 5

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")