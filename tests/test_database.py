from testing_data import TestingData
import pytest

class TestDatabase:

    @pytest.mark.parametrize('bun_index, expected_available_bun_name', [
        (0, TestingData.BLACK_BUN_NAME),
        (1, TestingData.WHITE_BUN_NAME),
        (2, TestingData.RED_BUN_NAME)
    ])

    def test_check_available_buns_in_the_list(self, db, bun_index, expected_available_bun_name):
        assert db.available_buns()[bun_index].name == expected_available_bun_name

    @pytest.mark.parametrize('ingredient_index, expected_available_ingredient_name', [
        (0, TestingData.HOT_SAUCE_NAME),
        (1, TestingData.SOUR_CREAM_NAME),
        (2, TestingData.CHILI_SAUCE_NAME),
        (3, TestingData.CUTLET_FILLING_NAME),
        (4, TestingData.DINOSAUR_FILLING_NAME),
        (5, TestingData.SAUSAGE_FILLING_NAME)
    ])

    def test_check_available_ingredient_in_the_list(self, db, ingredient_index, expected_available_ingredient_name):
        assert db.available_ingredient()[ingredient_index].name == expected_available_ingredient_name
