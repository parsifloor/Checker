#!/usr/bin/env python3


# This is entry point


from args_parser import parseIt
from get_values import saveData
from ugtelset_parser import getBalance

import os
import re
from colorama import Fore


def main():
    args = parseIt()

    if args.config and os.path.isfile('config.txt') is False:
        saveData()
    elif args.config and os.path.isfile('config.txt'):
        replace = input(Fore.RED + 'The config file exists, you needn`t do this. Replace the file?')
        if replace == 'y':
            saveData()
    elif os.path.isfile('config.txt'):
        with open('config.txt', 'r') as file:
            lines = file.readlines()
            login = re.sub('\n', '', lines[0])
            password = lines[1]
            getBalance(login, password)

if __name__ == "__main__":
    main()