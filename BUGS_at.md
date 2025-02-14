## Баг-репорт по итогам test run.

<span style="color:dimgray;">*Окружение:*</span>

* <span style="color:dimgray;">*Windows 10 Home Edition*</span>
* <span style="color:dimgray;">*python 3.13 // PyCharm 2024.1.6 (Community Edition)*</span>

---

| № дефекта | Описание | Шаги воспроизведения | Ожидаемый результат | Фактический результат |
| --- | --- | --- | --- | --- |
| BR.at_01 | При GET-запросе по item_id в качестве name возвращается значение item_id. <br /> ------- <br />**Severity:** <span style="color:red;">**major** </span><br />**Priority:** <span style="color:red;">**ASAP**</span> | 1\. Найти пользователя, у которого нет товаров. <br />2\. Создать у найденного пользователя новый товар.<br />3\. Сохранить id созданного объявления. <br />4\. Получить геттером созданное объявление.<br />5\. Сравнить отправленные данные с данными полученными через запрос по id объявления. | 1\. Объявление создается (код 200). <br />2\. Текст ответа "Сохранили объявление - {item_id}".<br />3\. Полученная информация совпадает с отправленной. | Полученная информация не совпадает с отправленной.<br />По ключу name возвращается значение item_id.<br /> |

```python
FAILURE: check name0 == 458dd496-2f52-455b-8286-0b8f2342d8a6: Wrong name in DB
```

| № дефекта | Описание | Шаги воспроизведения | Ожидаемый результат | Фактический результат |
| --- | --- | --- | --- | --- |
| BR.at_02 | При GET-запросе по sellerId в качестве id возвращается значение item_name<br /> ------- <br />**Severity:** <span style="color:red;"></span><span style="color:red;">**major**</span><span style="color:red;"> </span><br />**Priority:** <span style="color:red;"></span><span style="color:red;">**ASAP**</span> | 1\. Найти пользователя, у которого нет товаров. <br />2\. Создать у найденного пользователя новый товар.<br />3\. Сохранить id созданного объявления. <br />4\. Получить геттером созданное объявление.<br />5\. Сравнить отправленные данные с данными полученными через запрос по id объявления. | 1\. Объявление создается (код 200). <br />2\. Текст ответа "Сохранили объявление - {item_id}".<br />3\. Полученная информация совпадает с отправленной. | Полученная информация не совпадает с отправленной.<br />По ключу id возвращается значение name.<br /> |

```python
FAILURE: check 458dd496-2f52-455b-8286-0b8f2342d8a6 == dsdsd: Wrong item_id in DB
test_get_items_by_seller_id.py:46 in test_get_items_by_seller_id() -> check.equal(expected_item["item_id"], actual_item["id"], "Wrong item_id in DB")
```

| № дефекта | Описание | Шаги воспроизведения | Ожидаемый результат | Фактический результат |
| --- | --- | --- | --- | --- |
| BR.at_03 | При GET-запросе статистики по item_id возвращается неверное значение likes.<br /> ------- <br />**Severity:** <span style="color:darkgreen;">**minor**</span><br />**Priority:** <span style="color:red;"></span><span style="color:darkgreen;">**low**</span> | 1\. Создать новый товар.<br />2\. Сохранить статистику и uuid объявления. <br />3\. Получить данные о статистике объявления get-запросом.<br />4\. Сравнить статистику в отправленных и полученных данных. | 1\. Объявление создается (код 200). <br />2\. Текст ответа "Сохранили объявление - {item_id}".<br />3\. Полученная информация совпадает с отправленной. | Полученная информация не совпадает с отправленной.<br />Возвращается неверное значение likes. |

```python
FAILURE: check 8 == 16: Likes count isn't equal
test_get_stat_by_item_id.py:29 in test_get_stat_by_item_id() -> check.equal(expected_data[key], actual_data[key], f"{key.capitalize()} count isn't equal")
```

| № дефекта | Описание | Шаги воспроизведения | Ожидаемый результат | Фактический результат |
| --- | --- | --- | --- | --- |
| BR.at_04 | При GET-запросе статистики по item_id возвращается неверное значение viewCount.<br /> ------- <br />**Severity:** <span style="color:darkgreen;"></span><span style="color:darkgreen;">**medium**</span><br />**Priority:** <span style="color:darkgreen;"></span><span style="color:darkgreen;">**normal**</span><span style="color:red;"></span><span style="color:darkgreen;"></span> | 1\. Создать новый товар.<br />2\. Сохранить статистику и uuid объявления. <br />3\. Получить данные о статистике объявления get-запросом.<br />4\. Сравнить статистику в отправленных и полученных данных. | 1\. Объявление создается (код 200). <br />2\. Текст ответа "Сохранили объявление - {item_id}".<br />3\. Полученная информация совпадает с отправленной. | Полученная информация не совпадает с отправленной.<br />Возвращается неверное значение viewCount. |

```python
FAILURE: check 8 == 16: Likes count isn't equal
test_get_stat_by_item_id.py:29 in test_get_stat_by_item_id() -> check.equal(expected_data[key], actual_data[key], f"{key.capitalize()} count isn't equal")
```

| № дефекта | Описание | Шаги воспроизведения | Ожидаемый результат | Фактический результат |
| --- | --- | --- | --- | --- |
| BR.at_05 | При GET-запросе по item_id в качестве name возвращается "dsdsd".<br /> ------- <br />**Severity:** <span style="color:red;"></span><span style="color:red;">**major**</span><span style="color:red;"> </span><br />**Priority:** <span style="color:red;"></span><span style="color:red;">**ASAP**</span><span style="color:red;"></span><span style="color:darkgreen;"></span> | 1\. Найти продавца, у которого нет товаров.<br />2\. Создать новый товар.<br />3\. Сохранить id созданного объявления. <br />4\. Получить объявление get-запросом.<br />5\. Сравнить отправленные и полученные данные. | 1\. Объявление создается (код 200). <br />2\. Текст ответа "Сохранили объявление - {item_id}".<br />3\. Полученная информация совпадает с отправленной. | Полученная информация не совпадает с отправленной.<br />В поле name возвращается значение "dsdsd" вместо введенного. |

```python
FAILURE: check dsdsd == Number that product.: Item names aren't equal
test_get_item_by_id.py:25 in test_get_item_by_id() -> check.equal(got_item_data['name'], new_item_data["name"], msg="Item names aren't equal")  # Проверка названия item
```

| № дефекта | Описание | Шаги воспроизведения | Ожидаемый результат | Фактический результат |
| --- | --- | --- | --- | --- |
| BR.at_06 | При GET-запросе по sellerId в качестве name возвращается значение item_id.<br /> ------- <br />**Severity:** <span style="color:red;"></span><span style="color:red;">**major**</span><span style="color:red;"> </span><br />**Priority:** <span style="color:red;"></span><span style="color:red;">**ASAP**</span><span style="color:red;"></span><span style="color:darkgreen;"></span> | 1\. Найти продавца, у которого нет товаров. <br />2\. Сохранить id продавца.<br />3\. Создать у найденного продавца новый товар. <br />4\. Получить геттером по id продавца созданное объявление.<br />5\. Сравнить отправленные данные с данными полученными через запрос по id объявления. | 1\. Объявление создается (код 200). <br />2\. Текст ответа "Сохранили объявление - {item_id}".<br />3\. Полученная информация совпадает с отправленной. | Полученная информация не совпадает с отправленной.<br />В поле name возвращается значение item_id. |

```python
FAILURE: check 67c04c03-e241-4889-87d0-c30968451fe3 == Claim race.: Name isn't correct
test_post_new_item.py:31 in test_post_new_item() -> check.equal(actual_data[key], expected_data[key], f"{key.capitalize()} isn't correct")

```