import requests

domain = "https://api.vk.com/method"
access_token = "1c3bd0cd5c3ed1d72540d239cd0a587082807a8772d67994e450c3d442300d9f7cce22b2fdaacdfb2ea42"
user_id = "234889309"

query_params = {
    'domain' : domain,
    'access_token': access_token,
    'user_id': user_id,
    'fields': 'bdate'
}

query = "{domain}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v=5.74".format(**query_params)
response = requests.get(query)
list_friends = response.json()
sum = 0
n = 0

for i in range(list_friends["response"]["count"]):
    bdate = list_friends["response"]["items"][i].get("bdate", "None")
    if bdate != "None":
        s = bdate.split(".")
        for j in range(len(s)):
            if len(s[j]) == 4:
                sum += int(s[j])
                n += 1

print("Средний год рождения друзей:", round(sum / n))