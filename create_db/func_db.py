from .create_table import connection


def read():
    with connection.cursor() as cursor:
        cursor.execute("""SELECT * FROM google_api;""")
        info = [{'num': i[0], 'id': i[1], 'usd': i[2], 'rub': i[3], 'date': i[4]} for i in cursor.fetchall()]
        return info


def read_id():
    with connection.cursor() as cursor:
        cursor.execute("""SELECT id_order FROM google_api;""")
        id_data = [i[0] for i in cursor.fetchall()]
        return id_data


def add(data):
    print(data)
    id_order = data['id_order']
    usd_price = data['usd']
    pub_price = data['pub']
    delivery_time = data['time']
    if id_order not in read_id():
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO google_api(id_order, usd_price, pub_price, delivery_time) VALUES (%s, %s, %s, %s);", (id_order, usd_price, pub_price, delivery_time))
        print('Добавил')
    else:
        print('Уже есть')


def update(data):
    id = data['id']
    price = data['price']
    with connection.cursor() as cursor:
        cursor.execute("UPDATE google_api SET pub_price = (%s) WHERE id_order = (%s);", (price, id))
        print('Update')


def delete_sql(data):
    print(data)
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM google_api WHERE id_order = (%s)", (data,))
        print('delete')