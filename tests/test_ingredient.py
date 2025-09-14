from src.ingredient import Ingredient
from src.ingredient_type import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from testing_data import TestingData
import pytest

class TestIngredient:

    @pytest.mark.parametrize('name, price', [
        (TestingData.HOT_SAUCE_NAME, TestingData.HOT_SAUCE_PRICE),
        (TestingData.SOUR_CREAM_NAME, TestingData.SOUR_CREAM_PRICE),
        (TestingData.CHILI_SAUCE_NAME, TestingData.CHILI_SAUCE_PRICE)
    ])

    def test_get_price_of_ingredient_sauce(self, ingredient_sauce, name, price):
        ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, name, price)

        assert ingredient_sauce.get_price() == price

    @pytest.mark.parametrize('name, price', [
        (TestingData.HOT_SAUCE_NAME, TestingData.HOT_SAUCE_PRICE),
        (TestingData.SOUR_CREAM_NAME, TestingData.SOUR_CREAM_PRICE),
        (TestingData.CHILI_SAUCE_NAME, TestingData.CHILI_SAUCE_PRICE)
    ])        

    def test_get_name_of_ingredient_sauce(self, ingredient_sauce, name, price):
        ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, name, price)

        assert ingredient_sauce.get_name() == name

    @pytest.mark.parametrize('name, price', [
        (TestingData.HOT_SAUCE_NAME, TestingData.HOT_SAUCE_PRICE),
        (TestingData.SOUR_CREAM_NAME, TestingData.SOUR_CREAM_PRICE),
        (TestingData.CHILI_SAUCE_NAME, TestingData.CHILI_SAUCE_PRICE)
    ])

    def test_get_type_of_ingredient_sauce(self, ingredient_sauce, name, price):
        ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, name, price)

        assert ingredient_sauce.get_type() == INGREDIENT_TYPE_SAUCE

    @pytest.mark.parametrize('name, price', [
        (TestingData.CUTLET_FILLING_NAME, TestingData.CUTLET_FILLING_PRICE),
        (TestingData.DINOSAUR_FILLING_NAME, TestingData.DINOSAUR_FILLING_PRICE),
        (TestingData.SAUSAGE_FILLING_NAME, TestingData.SAUSAGE_FILLING_PRICE)
    ])

    def test_get_price_of_ingredient_filling(self, ingredient_filling, name, price):
        ingredient_filling = Ingredient(INGREDIENT_TYPE_FILLING, name, price)

        assert ingredient_filling.get_price() == price

    @pytest.mark.parametrize('name, price', [
        (TestingData.CUTLET_FILLING_NAME, TestingData.CUTLET_FILLING_PRICE),
        (TestingData.DINOSAUR_FILLING_NAME, TestingData.DINOSAUR_FILLING_PRICE),
        (TestingData.SAUSAGE_FILLING_NAME, TestingData.SAUSAGE_FILLING_PRICE)
    ])

    def test_get_name_of_ingredient_filling(self, ingredient_filling, name, price):
        ingredient_filling = Ingredient(INGREDIENT_TYPE_FILLING, name, price)

        assert ingredient_filling.get_name() == name

    @pytest.mark.parametrize('name, price', [
        (TestingData.CUTLET_FILLING_NAME, TestingData.CUTLET_FILLING_PRICE),
        (TestingData.DINOSAUR_FILLING_NAME, TestingData.DINOSAUR_FILLING_PRICE),
        (TestingData.SAUSAGE_FILLING_NAME, TestingData.SAUSAGE_FILLING_PRICE)
    ])

    def test_get_type_of_ingredient_filling(self, ingredient_filling, name, price):
        ingredient_filling = Ingredient(INGREDIENT_TYPE_FILLING, name, price)

        assert ingredient_filling.get_type() == INGREDIENT_TYPE_FILLING
