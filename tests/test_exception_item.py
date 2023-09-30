import pytest
from src.item import Item


def test_instantiate_csv():
    with pytest.raises(Exception):
        assert Item.instantiate_from_csv('../src/items.csv')
