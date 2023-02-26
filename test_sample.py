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

def test_calculate_taxes_based_on_location():
    items = [{"Name": "item1", "Price": 2, "Weight": 1.0, "Quantity": 8, "Location": "Canada"},
             {"Name": "item2", "Price": 9, "Weight": 0.2, "Quantity": 3, "Location": "Finland"}]
    expected_tax = 7.28
    assert calculate_taxes(items) == expected_tax
    assert round(calculate_total_cost(items, shipping=False) - calculate_base_price(items), 2) == expected_tax

def test_calculate_shipping_fees_based_on_location_and_weight():
    items = [{"Name": "item1", "Price": 45, "Weight": 2.4, "Quantity": 1, "Location": "Italy"},
             {"Name": "item2", "Price": 1, "Weight": 0.5, "Quantity": 20, "Location": "Spain"},
             {"Name": "item3", "Price": 15, "Weight": 3.8, "Quantity": 2, "Location": "Mauritania"}]
    expected_shipping_fees = 98.84
    assert calculate_shipping_fees(items) == expected_shipping_fees

def test_calculate_total_cost_with_taxes_and_shipping_fees():
    items = [{"Name": "item1", "Price": 14, "Weight": 2.9, "Quantity": 2, "Location": "Sweden"},
             {"Name": "item2", "Price": 9, "Weight": 0.2, "Quantity": 5, "Location": "Belgium"},
             {"Name": "item3", "Price": 3, "Weight": 0.9, "Quantity": 2, "Location": "Ghana"},
             {"Name": "item4", "Price": 4, "Weight": 0.5, "Quantity": 3, "Location": "South Africa"},
             {"Name": "item5", "Price": 11, "Weight": 0.1, "Quantity": 1, "Location": "Vietnam"}]
    expected_price = 165.04
    assert calculate_total_cost(items) == expected_price