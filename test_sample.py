from sample import *

def test_single_item_no_taxes_or_shipping():
    items = [{"Name": "item1", "Price": 10, "Weight": 0.5, "Quantity": 1, "Location": "Germany"}]
    expected_price = 10
    assert calculate_base_price(items) == expected_price
    assert calculate_total_cost(items, tax=False, shipping=False) == expected_price