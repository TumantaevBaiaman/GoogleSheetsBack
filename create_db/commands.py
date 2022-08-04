import pandas as pd

from googleAPI.table import gsheet2df
from create_db.func_db import add, update, read_id, delete_sql
from price import parser


def add_db():
    usd = parser.parser()
    print(usd)
    data_file = gsheet2df('google', 0)
    for i in data_file:
        print(i)
        info = {}
        info['id_order'] = i['заказ №']
        info['usd'] = i['стоимость,$']
        info['pub'] = i['стоимость,$'] * usd
        info['time'] = str(i['срок поставки'])
        add(info)


def update_db():
    usd = parser.parser()
    data_file = gsheet2df('google', 0)
    for i in data_file:
        info = {}
        info['id'] = i['заказ №']
        info['price'] = i['стоимость,$'] * usd
        info['usd'] = i['стоимость,$']
        update(info)


def delete_db():
    data_file = gsheet2df('google', 0)
    info = []
    data = read_id()
    for i in data_file:
        info.append(i['заказ №'])
    for i in data:
        if i in info:
            print('yes')
        elif i not in info:
            print('k')
            delete_sql(i)

