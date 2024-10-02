import random
import string
import requests
from data import Data


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = "".join(random.choice(letters) for i in range(length))
    return random_string


def generate_user_data():
    email = generate_random_string(6) + '@yandex.ru'
    password = generate_random_string(10)
    name = generate_random_string(10)
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    return payload


def created_orders(resp):
    token = resp.json().get("accessToken")
    ingredients = {"ingredients": [Data.FLUOR_BUN, Data.BIO_CUTLET, Data.SAUCE_SPICY]}
    headers = {"Content-type": "application/json", "Authorization": f'{token}'}
    response = requests.post(Data.CREATE_ORDER, headers=headers, json=ingredients)
    return response