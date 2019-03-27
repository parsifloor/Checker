import requests
import bs4
import re

login = 'uts11912'
password = '0301e3be'
url = 'http://lk.kbr.ugtelset.ru'
req = requests.post(url , {'username': login , 'password':password})
parsed = bs4.BeautifulSoup(req.text , 'html.parser')

summary = parsed.select('.label-success')
result = []
if len(summary) > 1:
	for summ in summary:
		result.append(summ.getText())
	result[1] = re.sub(' ' , '' , result[1])
	result[1] = re.sub('\n' , '' , result[1])
	print(result[0] , result[1])
else:
	result.append(summ.getText())
	print(result)
