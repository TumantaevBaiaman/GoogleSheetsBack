from .db_info import ip, user, password, db_name
import psycopg2


try:
    connection = psycopg2.connect(
        host=ip,
        user=user,
        password=password,
        database=db_name,
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"server version: {cursor.fetchone()}")
    print(connection.cursor())
    print('start')
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS google_api(
                id serial PRIMARY KEY,
                id_order bigint NOT NULL,
                usd_price bigint NOT NULL,
                pub_price NUMERIC (10, 3) NOT NULL,
                delivery_time varchar(50) NOT NULL
                );
                """
        )
    print('end')

except Exception as ex:
    print("Error")

finally:
    pass