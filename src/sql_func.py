import os
import sqlite3


def delete_table(file_db_name='db/users.db'):
    """
    Func delete the file database
    :return: message 'db delete'
    """
    try:
        return os.remove(file_db_name), print('db delete')
    except FileNotFoundError:
        return


def create_table_sql(file_db_name):
    """
    Create empty table.
    param file_db_name:
    :return: message 'Table city_name is created'
    """
    with sqlite3.connect(file_db_name) as db:
        cursor = db.cursor()
        query = f""" CREATE TABLE IF NOT EXISTS users(
        cell TEXT,
        dob_age REAL,
        dob_date TEXT,
        email TEXT,
        gender TEXT,
        id_name TEXT,
        id_value TEXT,
        location_city TEXT,
        location_coordinates_latitude TEXT,
        location_coordinates_longitude TEXT,
        location_country TEXT,
        location_postcode REAL,
        location_state TEXT,
        location_street_name TEXT,
        location_street_number REAL,
        location_timezone_description TEXT,
        location_timezone_offset TEXT,
        login_md5 TEXT,
        login_password TEXT,
        login_salt TEXT,
        login_sha1 TEXT,
        login_sha256 TEXT,
        login_username TEXT,
        login_uuid TEXT,
        name_first TEXT,
        name_last TEXT,
        name_title TEXT,
        nat TEXT,
        phone TEXT,
        picture_large TEXT,
        picture_medium TEXT, 
        picture_thumbnail TEXT,
        registered_age REAL,
        registered_date TEXT)
    """
        cursor.execute(query)
        db.commit()
    return print(f'Table users is created')


def added_info(data):
    """
    Added info to table.
    """
    with sqlite3.connect('db/users.db') as db:
        cursor = db.cursor()
    query = f"""INSERT INTO users VALUES( ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? ,
                                            ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? ); """
    cursor.executemany(query, (data,))
    db.commit()
    return print(f'added info users')
