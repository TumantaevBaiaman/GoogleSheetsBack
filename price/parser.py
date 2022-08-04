import requests
import xmltodict

from date.today import time


def parser():
    response = requests.Session().get('https://www.cbr.ru/scripts/XML_daily.asp?date_req='+str(time()))
    dict_data = xmltodict.parse(response.content)
    usd = ''
    for i in dict_data['ValCurs']['Valute']:
        if i['CharCode'] == 'USD':
            print(i)
            usd = i['Value']
    usd = usd.split(',')
    return float(usd[0]+'.'+usd[1])
