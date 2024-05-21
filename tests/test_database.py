from praktikum.database import Database


class TestDataBase:
    def test_available_buns_get_quantity_success(self):
        test_database = Database()
        assert len(test_database.available_buns()) == 3



    def test_available_ingredients_get_quantity_success(self):
        test_database = Database()
        assert len(test_database.available_ingredients()) == 6

