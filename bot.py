from cgitb import text

from keyboard import sender
from main import *


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        request = event.text.lower()
        user_id = str(event.user_id)
        msg = event.text.lower()
        sender(user_id, text)
        if request == 'начать поиск':
            bot.write_msg(user_id, f'Привет, {bot.get_name(user_id)}')
            bot.find_candidate(user_id)
            bot.write_msg(event.user_id, f'Нашёл для тебя пару')
            bot.found_person_info(user_id)

        elif request == 'посмотреть':
            for i in line:
                bot.found_person_info(user_id)
                break

        else:
            bot.write_msg(event.user_id, 'некорректные данные')

