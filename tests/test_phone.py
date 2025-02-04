from src.phone import Phone
from tests.test_item import item
import pytest


@pytest.fixture
def phone():
    return Phone("Телефон", 15_000, 10, 3)


def test_create_correct(phone):
    assert phone.name == "Телефон"
    assert phone.price == 15_000.0
    assert phone.quantity == 10
    assert phone.number_of_sim == 3


def test_create_incorrect():
    with pytest.raises(Exception):
        Phone(4, 15_000, 10, 3)

    with pytest.raises(Exception):
        Phone("Телефон", -15_000, 10, 3)

    with pytest.raises(Exception):
        Phone("Телефон_супертелефон_телефонище", 15_000, 10, 3)

    with pytest.raises(Exception):
        Phone("Телефон", 15_000, -10, 3)

    with pytest.raises(ValueError):
        Phone("Телефон", 15_000, 10, 0)


def test_repr(phone):
    assert repr(phone) == "Phone('Телефон', 15000.0, 10, 3)"


def test_str(phone):
    assert str(phone) == 'Телефон'


def test_add_item(phone, item):
    assert item + phone == 18
    assert phone + item == 18


def test_add_other(phone):
    with pytest.raises(TypeError):
        phone + 8

    with pytest.raises(TypeError):
        phone + "8"
