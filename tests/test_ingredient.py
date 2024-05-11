from data import DataTest
from praktikum.ingredient import Ingredient


class TestIngredient:
    def test_get_name_ingredient_success(self):
        test_ingredient = Ingredient(DataTest.test_ingredient_type,
                                     DataTest.test_ingredient_name,
                                     DataTest.test_ingredient_price)
        assert test_ingredient.get_name() == DataTest.test_ingredient_name




    def test_get_price_ingredient_success(self):
        test_ingredient = Ingredient(DataTest.test_ingredient_type,
                                     DataTest.test_ingredient_name,
                                     DataTest.test_ingredient_price)
        assert test_ingredient.get_price() == DataTest.test_ingredient_price




    def test_get_type_ingredient_success(self):
        test_ingredient = Ingredient(DataTest.test_ingredient_type,
                                     DataTest.test_ingredient_name,
                                     DataTest.test_ingredient_price)
        assert test_ingredient.get_type() == DataTest.test_ingredient_type

