import functions as f
import pytest_check as check


def test_get_item_by_id():
    """
    № тест-кейса: TC.AT_2
    Описание: Проверка идентичности отправленной информации и полученной информации об item.
    """
    # Создаем новый элемент
    created_item = f.create_item()

    # Извлекаем данные из ответа на создание элемента
    new_item_id = created_item["response"]["status"].split(" ")[-1]  # Получаем ID созданного элемента
    new_item_data = created_item["data"]  # Получаем данные, которые мы отправили при создании

    # Запрашиваем элемент по id
    got_item_response = f.get_items_by_id(new_item_id)
    check.equal(got_item_response.status_code, 200, msg="Status code isn't 200")  # Проверка статус-кода

    got_item_data = got_item_response.json()[0]

    # Проверяем соответствие данных
    check.equal(got_item_data['id'], new_item_id, msg="Item IDs aren't equal")  # Проверка item ID
    check.equal(got_item_data['name'], new_item_data["name"], msg="Item names aren't equal")  # Проверка названия item
    check.equal(got_item_data['price'], new_item_data["price"], msg="Item prices aren't equal")  # Проверка цены item
    check.equal(got_item_data['sellerId'], new_item_data["sellerID"], msg="Item seller_ids aren't equal")  # Проверка
    # seller_id item
    check.equal(got_item_data['statistics'], new_item_data["statistics"], msg="Item statistic data isn't equal")  #
    # Проверка статистики item
