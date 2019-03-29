import telebot

access_token = "570926580:AAHP6TIYvyLH6eYlqQWHBsQMtTDGGuMXcIw"
# Создание бота с указанным токеном доступа
bot = telebot.TeleBot(access_token)


# Бот будет отвечать только на текстовые сообщения
@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)

# import requests
#
#
# def get_page(group, week=''):
#     if week:
#         week = str(week) + '/'
#     url = '{domain}/{group}/{week}raspisanie_zanyatiy_{group}.htm'.format(
#         domain="http://www.ifmo.ru/ru/schedule/0",
#         week=week,
#         group=group)
#     response = requests.get(url)
#     web_page = response.text
#     return web_page
#
#
#
#
#
# def get_schedule(web_page):
#     soup = beautifulsoup4(web_page, "html5lib")
#
#     # Получаем таблицу с расписанием на понедельник
#     schedule_table = soup.find("table", attrs={"id": "1day"})
#
#     # Время проведения занятий
#     times_list = schedule_table.find_all("td", attrs={"class": "time"})
#     times_list = [time.span.text for time in times_list]
#
#     # Место проведения занятий
#     locations_list = schedule_table.find_all("td", attrs={"class": "room"})
#     locations_list = [room.span.text for room in locations_list]
#
#     # Название дисциплин и имена преподавателей
#     lessons_list = schedule_table.find_all("td", attrs={"class": "lesson"})
#     lessons_list = [lesson.text.split('\n\n') for lesson in lessons_list]
#     lessons_list = [', '.join([info for info in lesson_info if info]) for lesson_info in lessons_list]
#
#     return times_list, locations_list, lessons_list
#
# print(get_schedule(get_page("B3100", 0)))
