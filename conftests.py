import pytest
from tests.testing_data import TestingData
from src.bun import Bun
from src.ingredient import Ingredient
from src.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from src.database import Database
from src.burger import Burger
from unittest.mock import Mock

@pytest.fixture(scope='function')
def bun():
    test_bun = Bun(TestingData.BLACK_BUN_NAME, TestingData.BLACK_BUN_PRICE)
    return test_bun

@pytest.fixture(scope='function')
def ingredient_sauce():
    test_ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, TestingData.HOT_SAUCE_NAME, TestingData.HOT_SAUCE_PRICE)
    return test_ingredient_sauce

@pytest.fixture(scope='function')
def ingredient_filling():
    test_ingredient_filling = Ingredient(INGREDIENT_TYPE_FILLING, TestingData.CHILI_SAUCE_NAME, TestingData.CUTLET_FILLING_PRICE)
    return test_ingredient_filling

@pytest.fixture(scope='function')
def db():
    return Database()

@pytest.fixture(scope='function')
def burger():
    test_burger = Burger()
    return test_burger

@pytest.fixture(scope='function')
def mock():
    mock = Mock()
    return mock
