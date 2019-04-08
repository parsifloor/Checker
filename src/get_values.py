from colorama import Fore ,  init
import getpass

init(autoreset=True)

def getData():
    login = input(Fore.CYAN + 'Enter your login: ')
    password = getpass.getpass(Fore.CYAN + 'Enter your password: ')
    if True:
        print('\n' + Fore.GREEN + 'The basic config succesful ')
    return login , password

def saveData():
    data = getData()
    with open('config.txt' , 'w') as file:
        file.write(data[0] + '\n')
        file.write(data[1])

