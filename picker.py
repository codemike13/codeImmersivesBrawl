import subprocess
import random
import time
import sys
from termcolor import colored
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format


def whoUpDawg():
    names = [
        'Andrea',
        'Xiao',
        'Daramy',
        'Garuz',
        'Stilwell',
        'Niko',
        'Sung',
        'Daniel',
        'Rainer',
        'Rashaan'
    ]
    who = f'figlet -w 120 -f cybermedium "{names[random.randrange(10)]}"'
    clear = subprocess.call('clear', shell=True)
    sendIt = subprocess.call(who, shell=True)


whoUpDawg()
