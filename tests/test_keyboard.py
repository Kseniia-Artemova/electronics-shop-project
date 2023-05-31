from src.keyboard import Keyboard
import pytest


@pytest.fixture
def keyboard():
    return Keyboard('Dark Project KD87A', 3600, 19)


def test_create_correct(keyboard):
    assert keyboard.name == 'Dark Project KD87A'
    assert keyboard.price == 3600.0
    assert keyboard.quantity == 19
    assert keyboard.language == "EN"


def test_create_incorrect():
    with pytest.raises(ValueError):
        Keyboard(18, 3600, 19)

    with pytest.raises(Exception):
        Keyboard('Dark Project KD87A', "3600", 19)

    with pytest.raises(Exception):
        Keyboard('Dark Project KD87A', 3600, "19")


def test_change_lang(keyboard):
    keyboard.change_lang()
    assert keyboard.language == "RU"
    keyboard.change_lang()
    assert keyboard.language == "EN"
    keyboard.change_lang()
    assert keyboard.language == "RU"
    keyboard.change_lang()
    assert keyboard.language == "EN"
