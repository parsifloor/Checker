#!/usr/bin/env python3

import sys
import re

try:
	import requests
	import bs4
	from colorama import Fore , Style
except ImportError:
	print('The requirment doesn`t downloaded')
	sys.exit()



url = 'http://lk.kbr.ugtelset.ru'

def getBalance(login , password):
	req = requests.post(url , {'username': login , 'password':password})
	parsed = bs4.BeautifulSoup(req.text , 'html.parser')

	summary = parsed.select('.label-success')
	if len(summary) < 2:
		balanceValue = parsed.select('.label-warning')[0].getText()
		balanceStatus = summary[0].getText().strip()
		
		print(Fore.RED + 'Баланс лицевого счета: ' + balanceValue)
		print(Fore.GREEN + 'Статус: ' + balanceStatus)

	else:
		balanceValue = summary[0].getText()
		balanceStatus = summary[1].getText().strip()
	
		print(Fore.YELLOW + 'Баланс лицевого счета: ' + balanceValue)
		print(Fore.GREEN + 'Статус: ' + balanceStatus)


