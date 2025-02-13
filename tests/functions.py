import random
from pprint import pprint
import requests
from data import urls


def get_items_by_id(item_id):
    """Функция получает данные о item_id.
    Принимает item_id.
    Возвращает json по item."""
    response_func = requests.get(f'{urls.BASE_URL}/api/1/item/{item_id}')
    return response_func


def create_items():
    """
    Функция создает item.
    Значения seller_id, price случайны.
    Возвращает json по item и введенные данные.
    """
    seller_id = random.randint(111111, 999999)
    price = random.randint(1, 1000)
    data = {
        "sellerID": seller_id,
        "name": "book",
        "price": price,
        "statistics": {
            "contacts": 1,
            "likes": 2,
            "viewCount": 3
        }
    }

    response = requests.post(f"{urls.BASE_URL}/api/1/item", json=data)
    return response, data


def get_items_count(seller_id):
    """
    Функция определяет количество items у seller.
    Принимает seller_id.
    Возвращает количество items.
    """
    response = requests.get(f'{urls.BASE_URL}/api/1/{seller_id}/item')
    return len(response.json())


def find_unic_seller_id():
    """
    Функция находит seller, у которого нет items.
    Возвращает seller_id:int.
    """
    seller_id = random.randint(111111, 999999)
    # response = requests.get(f'{urls.BASE_URL}/api/1/seller/{seller_id}')
    response = requests.get(f'{urls.BASE_URL}/api/1/{seller_id}/item')
    items_count = len(response.json())
    if items_count == 0:
        return seller_id
    else:
        find_unic_seller_id()


def find_seller_id(seller_id):
    """
    Функция находит seller по seller_id.
    Возвращает sellers items.
    """
    response = requests.get(f'{urls.BASE_URL}/api/1/{seller_id}/item')
    return response


def create_items_by_unic_seller_id(seller_id=find_unic_seller_id()):
    """
    Функция создает item у seller, у которого нет items.
    Принимает seller_id, сгенерированный функцией find_unic_seller_id().
    Возвращает json ответа на post-запрос и введенные данные.
    """
    price = random.randint(1, 1000)
    data = {
        "sellerID": seller_id,
        "name": "another_book",
        "price": price,
        "statistics": {
            "contacts": 4,
            "likes": 5,
            "viewCount": 6
        }
    }
    response = requests.post(f"{urls.BASE_URL}/api/1/item", json=data)
    return response, data
