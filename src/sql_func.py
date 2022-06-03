import os
import sqlite3
from pprint import pprint


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
    return


def list_all_data_from_a_collection(file_db_name='db/users.db'):
    """
    function return all database objects
    :param file_db_name:
    :return: list
    """
    with sqlite3.connect(file_db_name) as db:
        cursor = db.cursor()
    query = f""" SELECT * FROM users; """
    cursor.execute(query)
    db.commit()
    data_list = (cursor.execute(query)).fetchall()
    # for i, v in enumerate(data_list):
    #     print(i+1, v)
    return data_list


def get_one_specified_entity(param='nat', param_data='AU', file_db_name='db/users.db'):
    """
    function search database objects
    :param param: search object
        cell, dob_age, dob_date, email, gender, id_name, id_value, location_city,
        location_coordinates_latitude, location_coordinates_longitude,
        location_country, location_postcode, location_state,
        location_street_name, location_street_number,
        location_timezone_description, location_timezone_offset,
        login_md5, login_password, login_salt, login_sha1,
        login_sha256, login_username, login_uuid,
        name_first, name_last, name_title, nat,
        phone,  picture_large, picture_medium, picture_thumbnail,
        registered_age, registered_date.
    :param param_data: name object
    :param file_db_name:
    :return:
    """
    with sqlite3.connect(file_db_name) as db:
        cursor = db.cursor()
    query = f""" SELECT * FROM users WHERE {param} = '{param_data}' ; """
    cursor.execute(query)
    db.commit()
    data_list = (cursor.execute(query)).fetchall()
    return data_list


def delete_one_specified_entity(param='nat', param_data='DE', file_db_name='db/users.db'):
    """
    function deletes database objects
    :param param: search object
    :param param_data: name object
    :param file_db_name:
    :return:
    """
    with sqlite3.connect(file_db_name) as db:
        cursor = db.cursor()
    query = f""" DELETE FROM users WHERE {param} = '{param_data}' ; """
    cursor.execute(query)
    db.commit()
    return print(f'{param} = {param_data} delete')


def print_to_json(data):
    json_list = {"results": []}
    for i, v in enumerate(data):
        user_json = {
            "gender": v[4],
            "name": {
                "title": v[26],
                "first": v[24],
                "last": v[25]
                },
            "location": {
                "street": {
                    "number": v[14],
                    "name": v[13]
                    },
                "city": v[7],
                "state": v[12],
                "country": v[10],
                "postcode": v[11],
                "coordinates": {
                    "latitude": v[8],
                    "longitude": v[9]
                    },
                "timezone": {
                    "offset": v[16],
                    "description": v[15]
                    }
                },
            "email": v[3],
            "login": {
                "uuid": v[23],
                "username": v[22],
                "password": v[18],
                "salt": v[19],
                "md5": v[17],
                "sha1": v[20],
                "sha256": v[21]
                },

            "dob": {
                "date": v[2],
                "age": v[1]
                },
            "registered": {
                "date": v[33],
                "age": v[32]
                },
            "phone": v[28],
            "cell": v[0],
            "id": {
                "name": v[5],
                "value": v[6]
                },
            "picture": {
                "large": v[29],
                "medium": v[30],
                "thumbnail": v[31]
                },
            "nat": v[27]
            }
        json_list['results'].append(user_json)
    return json_list


pprint(print_to_json(get_one_specified_entity('nat', 'US')))
# pprint(print_to_json(list_all_data_from_a_collection()))
