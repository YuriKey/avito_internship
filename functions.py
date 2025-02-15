import random
import requests
from data import urls
from faker import Faker

fake = Faker()


def make_request(method, url, json=None):
    """
    Выполняет запрос и возвращает ответ.
    :param method: Метод запроса (GET, POST и т.д.)
    :param url: URL для запроса
    :param json: JSON-данные для POST-запросов
    :return: Объект Response
    """
    return requests.request(method, url, json=json)


def get_items_by_id(item_id):
    """
    Получает объект по его ID.
    :param item_id: UUID сущности
    :return: Объект Response
    """
    url = f'{urls.BASE_URL}/api/1/item/{item_id}'
    return make_request('GET', url)


def get_items_by_seller(seller_id):
    """
    Получает список элементов, созданных конкретным продавцом.
    :param seller_id: ID продавца
    :return: Словарь с элементами и статус-кодом
    """
    url = f'{urls.BASE_URL}/api/1/{seller_id}/item'
    response = make_request('GET', url)
    return {"items": response.json(), "status_code": response.status_code}


def get_statistics(item_id):
    """
    Получает статистику по конкретному элементу.
    :param item_id: UUID элемента
    :return: Объект Response
    """
    url = f'{urls.BASE_URL}/api/1/statistic/{item_id}'
    return make_request('GET', url)


def get_unic_seller_id():
    """
    Находит продавца, у которого нет элементов.
    :return: ID продавца
    """
    while True:
        seller_id = random.randint(111111, 999999)
        url = f'{urls.BASE_URL}/api/1/{seller_id}/item'
        response = make_request('GET', url)
        if len(response.json()) == 0:
            return seller_id


def create_item(seller_id=None, price=None, name=None, statistics=None):
    """
    Создает новый элемент с заданными или случайными данными.
    :param seller_id: ID продавца
    :param price: Цена элемента
    :param name: Название элемента
    :param statistics: Статистика элемента
    :return: Словарь с ответом и входными данными
    """
    if not seller_id:
        seller_id = random.randint(111111, 999999)
    if not price:
        price = random.randint(1, 1000)
    if not name:
        name = fake.text(20)
    if not statistics:
        statistics = {
            "contacts": random.randint(1, 10),
            "likes": random.randint(1, 10),
            "viewCount": random.randint(1, 10)
        }

    data = {
        "sellerID": seller_id,
        "name": name,
        "price": price,
        "statistics": statistics
    }
    url = f"{urls.BASE_URL}/api/1/item"
    response = make_request('POST', url, json=data)
    return {
        "response": response.json(),
        "status_code": response.status_code,
        "data": data
    }


def create_item_by_unic_seller_id():
    """
    Создает элемент у продавца, у которого нет элементов.
    :return: Словарь с ответом и входными данными
    """
    seller_id = get_unic_seller_id()
    return create_item(seller_id=seller_id)
