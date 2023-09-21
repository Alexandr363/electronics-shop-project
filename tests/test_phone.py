from src.phone import Phone
import pytest

phone = Phone('tel', 10, 5, 1)


def test_phone_repr():
    assert repr(phone) == "Phone('tel', 10, 5, 1)"


def test_number_of_sim():
    assert phone.number_of_sim == 1


def test_setter_number_of_sim():
    phone.number_of_sim = 5
    assert phone.number_of_sim == 5
    phone.number_of_sim = 0
    with pytest.raises(Exception):
        ValueError('Количество физических SIM-карт '
                   'должно быть целым числом больше нуля')
