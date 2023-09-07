"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


item1 = Item('tel', 10, 5)
Item.pay_rate = 5


def test_calculate_total_price():
    assert item1.calculate_total_price() == 50


def test_apply_discount():
    item1.apply_discount()
    assert item1.price == 50
