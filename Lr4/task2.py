import requests
from pprint import pprint as pp
from datetime import datetime

domain = "https://api.vk.com/method"
access_token = "1c3bd0cd5c3ed1d72540d239cd0a587082807a8772d67994e450c3d442300d9f7cce22b2fdaacdfb2ea42"
user_id = "234889309"


def messages_get_history(user_id=329143903, offset=0, count=50):

    query_params = {
       'domain' : domain,
       'access_token': access_token,
        'user_id': user_id,
       'peer_id': user_id,
       'offset': offset,
        'count': count,
        'fields': 'bdate'
    }

    query = "{domain}/messages.getHistory?count={count}"\
            "&peer_id={peer_id}&access_token={access_token}"\
            "&user_id={user_id}&v=5.74".format(**query_params)
    response = requests.get(query)
    return response.json()


def count_dates_from_messages(messages):
    count = [0]
    dates = ['0']
    j = 0
    for i in range(len(messages)):
        message = messages[i]
        print(message)
        date = datetime.fromtimestamp(message['date']).strftime("%Y-%m-%d")
        if dates[j] != date:
            dates.append(date)
            count.append(1)
            j += 1
        else:
            count[j] += 1

    count.pop(0)
    dates.pop(0)

    return dates, count


history = messages_get_history()
messages = history['response']['items']
print(count_dates_from_messages(messages))
# date = datetime.fromtimestamp(message['date']).strftime("%Y-%m-%d")
# print(date)