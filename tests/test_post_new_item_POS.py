from tests import functions as f


def test_get_items_by_seller():
    actual_data = f.create_items_by_unic_seller_id(seller_id=f.find_unic_seller_id())
    expected_data = actual_data[1]
    item_id = actual_data[0].json()['status'].split(' ')[-1]
    seller_id = actual_data[1]['sellerID']
    database_data = f.get_items_by_id(item_id)
    data_by_seller_id = f.find_seller_id(seller_id)

    assert actual_data[0].status_code == 200, "Status code isn`t 200"
    assert data_by_seller_id.json()[0]['name'] == expected_data['name'], "Names aren`t equal"
    assert database_data.json()[0]['name'] == expected_data['name'], "Names aren`t equal"

    assert data_by_seller_id.json()[0]['price'] == expected_data['price'], "Prices aren`t equal"
    assert database_data.json()[0]['price'] == expected_data['price'], "Prices aren`t equal"

    assert data_by_seller_id.json()[0]['sellerId'] == expected_data['sellerID'], "Seller IDs aren`t equal"
    assert database_data.json()[0]['sellerId'] == expected_data['sellerID'], "Seller IDs aren`t equal"

    assert data_by_seller_id.json()[0]['statistics'] == expected_data['statistics'], "Statistic data isn`t equal"
    assert database_data.json()[0]['statistics'] == expected_data['statistics'], "Statistic data isn`t equal"

