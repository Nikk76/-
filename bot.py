from database import insert_data_seen_users
from main import *

offset = 0


def send_photo_1(user_id, message):
    vk.method("messages.send", {"user_id": user_id,
                                'access_token': user_token,
                                'message': message,
                                'attachment': f'photo{person_id(offset)}_{get_photo_1(person_id(offset))}',
                                "random_id": 0})


def send_photo_2(user_id, message):
    vk.method("messages.send", {"user_id": user_id,
                                'access_token': user_token,
                                'message': message,
                                'attachment': f'photo{person_id(offset)}_{get_photo_2(person_id(offset))}',
                                "random_id": 0})


def send_photo_3(user_id, message):
    vk.method("messages.send", {"user_id": user_id,
                                'access_token': user_token,
                                'message': message,
                                'attachment': f'photo{person_id(offset)}_{get_photo_3(person_id(offset))}',
                                "random_id": 0})


def find_persons(user_id, offset):
    write_msg(user_id, found_person_info(offset))
    person_id(offset)
    insert_data_seen_users(person_id(offset))
    get_photos_id(person_id(offset))
    send_photo_1(user_id, 'Фото 1')
    send_photo_2(user_id, 'Фото 2')
    send_photo_3(user_id, 'Фото 3')


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        request = event.text.lower()
        user_id = str(event.user_id)
        msg = event.text.lower()
        if request == 'начать поиск':
            write_msg(event.user_id, f'Привет, {get_name(user_id)}')
            write_msg(event.user_id, f'Нашёл пару, нажми "далее"')
            find_persons(user_id, offset)

        elif request == 'далее':
            offset += 1
            find_persons(user_id, offset)
            break
        elif request == 'назад':
            write_msg(user_id, 'далее')

        else:
            write_msg(event.user_id, 'некорректное сообщение')
