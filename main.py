import datetime

import requests
import vk_api
from select import select
from vk_api.longpoll import VkLongPoll, VkEventType

from database import insert_data_users

user_token = input('user_Token: ')
comm_token = input('comm_Token: ')


vk = vk_api.VkApi(token=comm_token)
longpoll = VkLongPoll(vk)


def write_msg(user_id, message):
    from random import randrange
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7)})


def get_name(user_id):
    url = f'https://api.vk.com/method/users.get'
    params = {'access_token': user_token,
              'user_ids': user_id,
              'v': '5.131'}
    repl = requests.get(url, params=params)
    response = repl.json()
    try:
        information_list = response['response']
        for i in information_list:
            for key, value in i.items():
                first_name = i.get('first_name')
                return first_name
    except KeyError:
        write_msg(user_id, 'ошибка токена')


def get_age(user_id):
    global date
    url = f'https://api.vk.com/method/users.get'
    params = {'access_token': user_token,
              'user_ids': user_id,
              'fields': 'bdate',
              'v': '5.131'}
    repl = requests.get(url, params=params)
    response = repl.json()
    try:
        information_list = response['response']
        for i in information_list:
            date = i.get('bdate')
        date_list = date.split('.')
        if len(date_list) == 3:
            year = int(date_list[2])
            year_now = int(datetime.date.today().year)
            return year_now - year
    except KeyError:
        write_msg(user_id, 'ошибка токена')


def get_sex(user_id):
    url = f'https://api.vk.com/method/users.get'
    params = {'access_token': user_token,
              'user_ids': user_id,
              'fields': 'sex',
              'v': '5.131'}
    repl = requests.get(url, params=params)
    response = repl.json()
    try:
        information_list = response['response']
        for i in information_list:
            for key, value in i.items():
                find_sex = i.get('sex')
                return find_sex
    except KeyError:
        write_msg(user_id, 'ошибка токена')


def get_city(user_id, city_name):
    url = url = f'https://api.vk.com/method/database.getCities'
    params = {'access_token': user_token,
              'user_ids': user_id,
              'fields': 'city',
              'v': '5.131'}
    repl = requests.get(url, params=params)
    response = repl.json()
    try:
        information_list = response['response']
        for i in information_list:
            for key, value in i.items():
                find_city = i.get('city')
                return find_city
    except KeyError:
        write_msg(user_id, 'ошибка токена')


def marital_status(user_id):
    url = f'https://api.vk.com/method/users.get'
    params = {'access_token': user_token,
              'user_ids': user_id,
              'fields': 'relation',
              'v': '5.131'}
    repl = requests.get(url, params=params)
    response = repl.json()
    try:
        information_list = response['response']
        for i in information_list:
            for key, value in i.items():
                result = i.get('relation')
                return result
    except KeyError:
        write_msg(user_id, 'ошибка токена')


def find_candidate(user_id):
    url = f'https://api.vk.com/method/users.search'
    params = {'access_token': user_token,
              'v': '5.131',
              'name': get_name(user_id),
              'sex': get_sex(user_id),
              'age': get_age(user_id),
              'city': get_city(user_id),
              'status': marital_status(user_id),
              'count': 100}
    resp = requests.get(url, params=params)
    resp_json = resp.json()
    try:
        dict_1 = resp_json['response']
        list_1 = dict_1['items']
        for person_dict in list_1:
            first_name = person_dict.get('first_name')
            last_name = person_dict.get('last_name')
            vk_id = str(person_dict.get('id'))
            vk_link = 'vk.com/id' + str(person_dict.get('id'))
            insert_data_users(first_name, last_name, vk_id, vk_link)
        return f'Поиск завершён'
    except KeyError:
        write_msg(user_id, 'ошибка токена')


def get_photos_id(user_id):
    url = 'https://api.vk.com/method/photos.getAll'
    params = {'access_token': user_token,
              'type': 'album',
              'owner_id': user_id,
              'extended': 1,
              'count': 25,
              'v': '5.131'}
    resp = requests.get(url, params=params)
    dict_photos = dict()
    resp_json = resp.json()
    try:
        dict_1 = resp_json['response']
        list_1 = dict_1['items']
        for i in list_1:
            photo_id = str(i.get('id'))
            i_likes = i.get('likes')
            if i_likes.get('count'):
                likes = i_likes.get('count')
                dict_photos[likes] = photo_id
        list_of_ids = sorted(dict_photos.items(), reverse=True)
        return list_of_ids
    except KeyError:
        write_msg(user_id, 'ошибка токена')


def get_photo_1(user_id):
    list = user_id.get_photos_id(user_id)
    count = 0
    for i in list:
        count += 1
        if count == 1:
            return i[1]


def get_photo_2(user_id):
    list = user_id.get_photos_id(user_id)
    count = 0
    for i in list:
        count += 1
        if count == 2:
            return i[1]


def get_photo_3(user_id):
    list = user_id.get_photos_id(user_id)
    count = 0
    for i in list:
        count += 1
        if count == 3:
            return i[1]


def found_person_info(offset):
    tuple = select(offset)
    list = []
    for i in tuple:
        list.append(i)
    return f'{list[0]} {list[1]} {list[2]}'


def person_id(offset):
    tuple = select(offset)
    list = []
    for i in tuple:
        list.append(i)
    return str(list[2])


print('Bot was created')

