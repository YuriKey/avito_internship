from tests import functions as f
import pytest_check as check


def test_post_new_item():
    """
    № тест-кейса: TC.AT_1
    Описание: Создание нового товара. Проверка идентичности отправляемой информации и информации, получаемой от API.
    """
    created_item = f.create_item_by_unic_seller_id()

    # Извлекаем данные из ответа на создание элемента
    expected_data = created_item["data"]  # Сохраняем отправленные данные
    seller_id = expected_data["sellerID"]  # Получаем ID продавца

    # Получаем список товаров по seller_id
    items_by_seller = f.get_items_by_seller(seller_id)
    check.equal(items_by_seller["status_code"], 200, "Status code isn't 200")  # Проверяем статус-код ответа

    actual_data = items_by_seller["items"][0]

    # Добавляем seller_id в фактические данные для корректного сравнения
    actual_data["sellerID"] = seller_id

    # Сравниваем отправленные и полученные данные
    for key in expected_data:
        if key == "statistics":  # Для статистики сравниваем значения ключей
            for stat_key in expected_data[key]:
                check.equal(actual_data[key][stat_key], expected_data[key][stat_key], f"{stat_key.capitalize()} count isn't correct")
        else:
            check.equal(actual_data[key], expected_data[key], f"{key.capitalize()} isn't correct")