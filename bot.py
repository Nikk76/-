from cgitb import text
from main import get_city
from keyboard import sender
from main import *


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        request = event.text.lower()
        user_id = str(event.user_id)
        msg = event.text.lower()
        sender(user_id, text)
        if request == 'начать поиск':
            write_msg(user_id, f'Привет, {get_name(user_id)}')
            find_candidate(user_id)
            write_msg(event.user_id, f'Нашёл для тебя пару')
            found_person_info(user_id)

        elif request == 'посмотреть':
            for i in line:
                found_person_info(user_id)
                break

        else:
            write_msg(event.user_id, 'некорректные данные')