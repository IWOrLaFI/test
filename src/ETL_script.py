from sql_func import added_info

import requests


def request_to_api():
    """
    request to api https://randomuser.me/
    return: dict users
    """
    url = f'https://randomuser.me/api/?results=100&gender=male'
    return requests.get(url).json()


data = request_to_api()


class User:
    def __init__(self, cell, dob_age, dob_date, email, gender, id_name: None, id_value: None,
                 location_city, location_coordinates_latitude, location_coordinates_longitude,
                 location_country, location_postcode, location_state, location_street_name, location_street_number,
                 location_timezone_description, location_timezone_offset,
                 login_md5, login_password, login_salt, login_sha1, login_sha256, login_username, login_uuid,
                 name_first, name_last, name_title, nat, phone,
                 picture_large, picture_medium, picture_thumbnail,
                 registered_age, registered_date):
        self.cell = cell
        self.dob_age = dob_age
        self.dob_date = dob_date
        self.email = email
        self.gender = gender
        self.id_name = id_name
        self.id_value = id_value
        self.location_city = location_city
        self.location_coordinates_latitude = location_coordinates_latitude
        self.location_coordinates_longitude = location_coordinates_longitude
        self.location_country = location_country
        self.location_postcode = location_postcode
        self.location_state = location_state
        self.location_street_name = location_street_name
        self.location_street_number = location_street_number
        self.location_timezone_description = location_timezone_description
        self.location_timezone_offset = location_timezone_offset
        self.login_md5 = login_md5
        self.login_password = login_password
        self.login_salt = login_salt
        self.login_sha1 = login_sha1
        self.login_sha256 = login_sha256
        self.login_username = login_username
        self.login_uuid = login_uuid
        self.name_first = name_first
        self.name_last = name_last
        self.name_title = name_title
        self.nat = nat
        self.phone = phone
        self.picture_large = picture_large
        self.picture_medium = picture_medium
        self.picture_thumbnail = picture_thumbnail
        self.registered_age = registered_age
        self.registered_date = registered_date


def func():
    for i, value in enumerate(data['results']):
        u = User(
            value['cell'],
            value['dob']['age'],
            value['dob']['date'],
            value['email'],
            value['gender'],
            value['id']['name'],
            value['id']['value'],
            value['location']['city'],
            value['location']['coordinates']['latitude'],
            value['location']['coordinates']['longitude'],
            value['location']['country'],
            value['location']['postcode'],
            value['location']['state'],
            value['location']['street']['name'],
            value['location']['street']['number'],
            value['location']['timezone']['description'],
            value['location']['timezone']['offset'],
            value['login']['md5'],
            value['login']['password'],
            value['login']['salt'],
            value['login']['sha1'],
            value['login']['sha256'],
            value['login']['username'],
            value['login']['uuid'],
            value['name']['first'],
            value['name']['last'],
            value['name']['title'],
            value['nat'],
            value['phone'],
            value['picture']['large'],
            value['picture']['medium'],
            value['picture']['thumbnail'],
            value['registered']['age'],
            value['registered']['date']
        )
        us = [u.cell, u.dob_age, u.dob_date, u.email, u.gender, u.id_name, u.id_value,
              u.location_city, u.location_coordinates_latitude, u.location_coordinates_longitude,
              u.location_country, u.location_postcode, u.location_state, u.location_street_name,
              u.location_street_number,
              u.location_timezone_description, u.location_timezone_offset,
              u.login_md5, u.login_password, u.login_salt, u.login_sha1, u.login_sha256, u.login_username,
              u.login_uuid, u.name_first, u.name_last, u.name_title, u.nat, u.phone,
              u.picture_large, u.picture_medium, u.picture_thumbnail,
              u.registered_age, u.registered_date]
        added_info(us)


func()
# print(type(user_1), user_1)
