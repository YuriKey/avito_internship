import functions as f
import pytest_check as check


def test_get_items_by_seller_id():
    """
    № тест-кейса: TC.AT_4
    Описание: Проверка получения списка элементов по seller_id.
    """
    # Находим уникальный seller_id без элементов
    seller_id = f.get_unic_seller_id()

    # Создаем список ожидаемых элементов
    expected_items = []
    for i in range(2):
        price = 100 * (2 ** i)
        name = f"name{i}"
        created_item = f.create_item(seller_id=seller_id, price=price, name=name)

        # Извлекаем данные созданного элемента
        item_id = created_item["response"]["status"].split(" ")[-1]
        item_data = created_item["data"]

        # Формируем ожидаемые данные для проверки
        expected_item = {
            "item_id": item_id,
            "name": item_data["name"],
            "price": item_data["price"],
            "seller_id": item_data["sellerID"]
        }
        expected_items.append(expected_item)

    # Получаем элементы по seller_id
    response_by_seller = f.get_items_by_seller(seller_id)
    check.equal(200, response_by_seller["status_code"], "Status code isn't OK")  # Проверка статус-кода
    actual_items = response_by_seller["items"]

    # Проверяем общее количество элементов
    check.equal(len(expected_items), len(actual_items), "Wrong items count")

    # Проверяем каждый элемент
    for i, expected_item in enumerate(expected_items):
        actual_item = actual_items[i]

        # Проверяем соответствие данных
        check.equal(expected_item["item_id"], actual_item["id"], "Wrong item_id in DB")
        check.equal(expected_item["name"], actual_item["name"], "Wrong name in DB")
        check.equal(expected_item["price"], actual_item["price"], "Wrong price in DB")
        check.equal(expected_item["seller_id"], actual_item["sellerId"], "Wrong seller_id in DB")