from tests import functions as f
import pytest_check as check


def test_get_stat_by_item_id():
    """
    № тест-кейса: TC.AT_3
    Описание: Получение статистики по ID товара.
    """
    # Создаем элемент у уникального продавца
    created_item = f.create_item_by_unic_seller_id()

    # Извлекаем данные из ответа на создание элемента
    item_id = created_item["response"]["status"].split(" ")[-1]  # Получаем ID созданного элемента
    response_message = created_item["response"]["status"]  # Получаем текст сообщения от сервера
    expected_data = created_item["data"]["statistics"]  # Сохраняем отправленные значения статистики

    # Получаем статистику элемента из DB
    statistics_response = f.get_statistics(item_id)
    check.equal(statistics_response.status_code, 200, "Status code isn't 200")  # Проверяем код ответа

    actual_data = statistics_response.json()[0]

    # Проверяем сообщение сервера
    check.equal(response_message, f"Сохранили объявление - {item_id}", "Status message isn't correct")

    # Сравниваем значения ключей в словарях
    for key in expected_data:
        check.equal(expected_data[key], actual_data[key], f"{key.capitalize()} count isn't equal")