from sample import *

def test_single_item_no_taxes_or_shipping():
    items = [{"Name": "item1", "Price": 10, "Weight": 0.5, "Quantity": 1, "Location": "Germany"}]
    expected_price = 10
    assert calculate_base_price(items) == expected_price
    assert calculate_total_cost(items, tax=False, shipping=False) == expected_price

def test_multiple_items_no_taxes_or_shipping():
    items = [{"Name": "item1", "Price": 6, "Weight": 1.8, "Quantity": 2, "Location": "Germany"},
             {"Name": "item2", "Price": 4, "Weight": 0.7, "Quantity": 3, "Location": "Colombia"},
             {"Name": "item3", "Price": 9, "Weight": 2.0, "Quantity": 1, "Location": "Colombia"}]
    expected_price = 33
    assert calculate_base_price(items) == expected_price
    assert calculate_total_cost(items, tax=False, shipping=False) == expected_price