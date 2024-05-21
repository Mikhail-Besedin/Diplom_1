import pytest

from data import DataTest
from praktikum.burger import Burger


class TestBurger:

    def test_set_buns_in_burger_success(self, create_bun):
        test_burger = Burger()
        test_burger.set_buns(create_bun)
        assert test_burger.bun == create_bun


    @pytest.mark.parametrize("test_ingredient", [
        "create_ingredient_first",
        "create_ingredient_second"])
    def test_add_ingredient_in_burger_success(self, test_ingredient):
        test_burger = Burger()
        test_burger.add_ingredient(test_ingredient)
        assert test_ingredient in list(test_burger.ingredients)


    def test_remove_ingredient_in_burger_success(self, create_ingredient_first, create_ingredient_second):
        test_burger = Burger()
        test_burger.add_ingredient(create_ingredient_first)
        test_burger.add_ingredient(create_ingredient_second)
        test_burger.remove_ingredient(1)
        assert len(test_burger.ingredients) == 1 and create_ingredient_second not in list(test_burger.ingredients)


    def test_move_ingredient_in_burger_success(self, create_ingredient_first, create_ingredient_second):
        test_burger = Burger()
        test_burger.add_ingredient(create_ingredient_first)
        test_burger.add_ingredient(create_ingredient_second)
        test_burger.move_ingredient(1, 0)
        assert create_ingredient_second == test_burger.ingredients[0]


    def test_get_price_burger_success(self, create_bun, create_ingredient_first, create_ingredient_second):
        test_burger = Burger()
        test_burger.set_buns(create_bun)
        test_burger.add_ingredient(create_ingredient_first)
        test_burger.add_ingredient(create_ingredient_second)
        assert test_burger.get_price() == DataTest.burger_price


    def test_get_receipt_burger_success(self, create_bun, create_ingredient_first, create_ingredient_second):
        test_burger = Burger()
        test_burger.set_buns(create_bun)
        test_burger.add_ingredient(create_ingredient_first)
        test_burger.add_ingredient(create_ingredient_second)
        receipt = f'''(==== {test_burger.bun.get_name()} ====)
= {str(create_ingredient_first.get_type())} {create_ingredient_first.get_name()} =
= {str(create_ingredient_second.get_type())} {create_ingredient_second.get_name()} =
(==== {test_burger.bun.get_name()} ====)'''
        assert receipt in test_burger.get_receipt()
