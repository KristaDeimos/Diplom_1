from testing_data import TestingData
from src.bun import Bun
from src.ingredient import Ingredient
from src.ingredient_type import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import pytest

class TestBurger:

    @pytest.mark.parametrize('name, price', [
        (TestingData.BLACK_BUN_NAME, TestingData.BLACK_BUN_PRICE),
        (TestingData.WHITE_BUN_NAME, TestingData.WHITE_BUN_PRICE),
        (TestingData.RED_BUN_NAME, TestingData.RED_BUN_PRICE)
    ])

    def test_set_buns_to_burger(self, mock, burger, name, price):
        mock.get_name.return_value = name
        mock.get_price.return_value = price
        burger.set_buns(mock)

        assert burger.bun.get_name() == name and burger.bun.get_price() == price

    @pytest.mark.parametrize('name, price', [
        (TestingData.HOT_SAUCE_NAME, TestingData.HOT_SAUCE_PRICE),
        (TestingData.SOUR_CREAM_NAME, TestingData.SOUR_CREAM_PRICE),
        (TestingData.CHILI_SAUCE_NAME, TestingData.CHILI_SAUCE_PRICE),
        (TestingData.CUTLET_FILLING_NAME, TestingData.CUTLET_FILLING_PRICE),
        (TestingData.DINOSAUR_FILLING_NAME, TestingData.DINOSAUR_FILLING_PRICE),
        (TestingData.SAUSAGE_FILLING_NAME, TestingData.SAUSAGE_FILLING_PRICE)
    ])

    def test_add_ingredient_to_burger(self, mock, burger, name, price):
        mock.get_name.return_value = name
        mock.get_price.return_value = price
        burger.add_ingredients(mock)

        assert burger.ingredients == [mock]

    @pytest.mark.parametrize('name, price', [
        (TestingData.HOT_SAUCE_NAME,  TestingData.HOT_SAUCE_NAME),
        (TestingData.SOUR_CREAM_NAME, TestingData.SOUR_CREAM_PRICE),
        (TestingData.CHILI_SAUCE_NAME, TestingData.CHILI_SAUCE_PRICE),
        (TestingData.CUTLET_FILLING_NAME, TestingData.CUTLET_FILLING_PRICE),
        (TestingData.DINOSAUR_FILLING_NAME, TestingData.DINOSAUR_FILLING_PRICE),
        (TestingData.SAUSAGE_FILLING_NAME, TestingData.SAUSAGE_FILLING_PRICE)
    ])

    def test_remove_ingredient_from_burger(self, mock, burger, name, price):
        mock.get_name.return_value = name
        mock.get_price.return_value = price
        burger.add_ingredients(mock)
        burger.remove_ingredients(0)

        assert burger.ingredients == []

    @pytest.mark.parametrize('name, price', [
        (TestingData.HOT_SAUCE_NAME, TestingData.HOT_SAUCE_PRICE),
        (TestingData.SOUR_CREAM_NAME, TestingData.SOUR_CREAM_PRICE),
        (TestingData.CHILI_SAUCE_NAME, TestingData.CHILI_SAUCE_PRICE),
        (TestingData.CUTLET_FILLING_NAME, TestingData.CUTLET_FILLING_PRICE),
        (TestingData.DINOSAUR_FILLING_NAME, TestingData.DINOSAUR_FILLING_PRICE),
        (TestingData.SAUSAGE_FILLING_NAME, TestingData.SAUSAGE_FILLING_PRICE)
    ])

    def test_move_ingredient_in_burger(self, burger, ingredient_type, name_0, price_0, name_1, price_1):
        ingredient_0 = Ingredient(ingredient_type, name_0, price_0)
        ingredient_1 = Ingredient(ingredient_type, name_1, price_1)
        burger.add_ingredient(ingredient_0)
        burger.add_ingredient(ingredient_1)
        burger.move_ingredient(0, 1)

        assert burger.ingredients[1].name == ingredient_0.name
        assert burger.ingredients[0].name == ingredient_1.name

    @pytest.mark.parametrize('name, price', [
        (TestingData.BLACK_BUN_NAME, TestingData.BLACK_BUN_PRICE),
        (TestingData.WHITE_BUN_NAME, TestingData.WHITE_BUN_PRICE),
        (TestingData.RED_BUN_NAME, TestingData.RED_BUN_PRICE)
    ])

    @pytest.mark.parametrize('name, price', [
        (TestingData.HOT_SAUCE_NAME, TestingData.HOT_SAUCE_PRICE),
        (TestingData.SOUR_CREAM_NAME, TestingData.SOUR_CREAM_PRICE),
        (TestingData.CHILI_SAUCE_NAME, TestingData.CHILI_SAUCE_PRICE),
        (TestingData.CUTLET_FILLING_NAME, TestingData.CUTLET_FILLING_PRICE),
        (TestingData.DINOSAUR_FILLING_NAME, TestingData.DINOSAUR_FILLING_PRICE),
        (TestingData.SAUSAGE_FILLING_NAME, TestingData.SAUSAGE_FILLING_PRICE)
    ])

    def test_get_price_of_burger(self, burger, bun, bun_name, bun_price, ingredient, ingredient_name, ingredient_price, ingredient_type):
        bun = Bun(bun_name, bun_price)
        burger.set_buns(bun)
        burger.add_ingredients = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        expected_price = bun_price * 2 + ingredient_price

        assert burger.get_price() == expected_price

    @pytest.mark.parametrize('bun_name, bun_price', [
        (TestingData.BLACK_BUN_NAME, TestingData.BLACK_BUN_PRICE),
        (TestingData.WHITE_BUN_NAME, TestingData.WHITE_BUN_PRICE),
        (TestingData.RED_BUN_NAME, TestingData.RED_BUN_PRICE)
    ])
    
    def test_get_receipt_of_burger_with_only_buns(self, burger, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        burger.set_buns(bun)
        expected_receipt = f'(==== {bun.get_name()} ====)\n(==== {bun.get_name()} ====)\n\nPrice: {bun.get_price() * 2}'
        
        assert burger.get_receipt() == expected_receipt


    @pytest.mark.parametrize('bun_name, bun_price', [
        (TestingData.BLACK_BUN_NAME, TestingData.BLACK_BUN_PRICE),
        (TestingData.WHITE_BUN_NAME, TestingData.WHITE_BUN_PRICE),
        (TestingData.RED_BUN_NAME, TestingData.RED_BUN_PRICE)
    ])
    @pytest.mark.parametrize('ingredient_type, ingredient_name, ingredient_price', [
        (INGREDIENT_TYPE_SAUCE, TestingData.HOT_SAUCE_NAME, TestingData.HOT_SAUCE_PRICE),
        (INGREDIENT_TYPE_SAUCE, TestingData.SOUR_CREAM_NAME, TestingData.SOUR_CREAM_PRICE),
        (INGREDIENT_TYPE_SAUCE, TestingData.CHILI_SAUCE_NAME, TestingData.CHILI_SAUCE_PRICE),
        (INGREDIENT_TYPE_FILLING, TestingData.CUTLET_FILLING_NAME, TestingData.CUTLET_FILLING_PRICE),
        (INGREDIENT_TYPE_FILLING, TestingData.DINOSAUR_FILLING_NAME, TestingData.DINOSAUR_FILLING_PRICE),
        (INGREDIENT_TYPE_FILLING, TestingData.SAUSAGE_FILLING_NAME, TestingData.SAUSAGE_FILLING_PRICE)
    ])

    def test_get_receipt_of_burger_with_buns_and_one_ingredient(self, burger, bun_name, bun_price, ingredient_type, ingredient_name, ingredient_price):
        bun = Bun(bun_name, bun_price)
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        expected_receipt = (
            f"(==== {bun.get_name()} ====)\n"
            f"= {str(ingredient_type).lower()} {ingredient_name} =\n"
            f"(==== {bun.get_name()} ====)\n"
            f"\nPrice: {bun.get_price() * 2 + ingredient_price}"
        )
        
        assert burger.get_receipt() == expected_receipt


    @pytest.mark.parametrize('bun_name, bun_price', [
        (TestingData.BLACK_BUN_NAME, TestingData.BLACK_BUN_PRICE),
        (TestingData.WHITE_BUN_NAME, TestingData.WHITE_BUN_PRICE),
        (TestingData.RED_BUN_NAME, TestingData.RED_BUN_PRICE)
    ])
    
    @pytest.mark.parametrize('ingredient_type_1, ingredient_name_1, ingredient_price_1', [
        (INGREDIENT_TYPE_SAUCE, TestingData.HOT_SAUCE_NAME, TestingData.HOT_SAUCE_PRICE),
        (INGREDIENT_TYPE_SAUCE, TestingData.SOUR_CREAM_NAME, TestingData.SOUR_CREAM_PRICE),
        (INGREDIENT_TYPE_SAUCE, TestingData.CHILI_SAUCE_NAME, TestingData.CHILI_SAUCE_PRICE)
    ])
    
    @pytest.mark.parametrize('ingredient_type_2, ingredient_name_2, ingredient_price_2', [
        (INGREDIENT_TYPE_FILLING, TestingData.CUTLET_FILLING_NAME, TestingData.CUTLET_FILLING_PRICE),
        (INGREDIENT_TYPE_FILLING, TestingData.DINOSAUR_FILLING_NAME, TestingData.DINOSAUR_FILLING_PRICE),
        (INGREDIENT_TYPE_FILLING, TestingData.SAUSAGE_FILLING_NAME, TestingData.SAUSAGE_FILLING_PRICE)
    ])
    
    def test_get_receipt_multiple_ingredients(self, burger, bun_name, bun_price, 
                                          ingredient_type_1, ingredient_name_1, ingredient_price_1,
                                          ingredient_type_2, ingredient_name_2, ingredient_price_2):
        bun = Bun(bun_name, bun_price)
        ingredient_1 = Ingredient(ingredient_type_1, ingredient_name_1, ingredient_price_1)
        ingredient_2 = Ingredient(ingredient_type_2, ingredient_name_2, ingredient_price_2)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        expected_receipt = (
            f"(==== {bun.get_name()} ====)\n"
            f"= {str(ingredient_type_1).lower()} {ingredient_name_1} =\n"
            f"= {str(ingredient_type_2).lower()} {ingredient_name_2} =\n"
            f"(==== {bun.get_name()} ====)\n"
            f"\nPrice: {bun.get_price() * 2 + ingredient_price_1 + ingredient_price_2}"
        )
        
        assert burger.get_receipt() == expected_receipt    
