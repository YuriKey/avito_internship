from tests import functions as f


def test_get_item_by_id():
    create_data = f.create_items()
    new_item_id = create_data[0].json()['status'].split(' ')[-1]
    new_item_data = create_data[1]

    got_item_data = f.get_items_by_id(new_item_id).json()[0]

    assert create_data[0].status_code == 200, "Status code is not 200"
    assert got_item_data['id'] == new_item_id, "Item IDs aren`t not equal"
    assert got_item_data['name'] == new_item_data["name"], "Item names aren`t equal"
    assert got_item_data['price'] == new_item_data["price"], "Item prices aren`t equal"
    assert got_item_data['sellerId'] == new_item_data["sellerID"], "Item seller_ids aren`t equal"
    assert got_item_data['statistics'] == new_item_data["statistics"], "Item statistic data is not equal"
