from data import DataTest
from praktikum.bun import Bun


class TestBun:
    def test_get_name_bun_success(self):
        test_bun = Bun(DataTest.test_bun_name,DataTest.test_bun_price)
        assert test_bun.get_name() == DataTest.test_bun_name



    def test_get_price_bun_success(self):
        test_bun = Bun(DataTest.test_bun_name,DataTest.test_bun_price)
        assert test_bun.get_price() == DataTest.test_bun_price

