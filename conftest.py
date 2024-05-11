from unittest.mock import Mock
import pytest

from data import DataTest


@pytest.fixture()
def create_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = DataTest.test_bun_name
    mock_bun.get_price.return_value =DataTest.test_bun_price
    return mock_bun




@pytest.fixture(scope='function')
def create_ingredient_first():
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = DataTest.test_ingredient_name
    mock_ingredient.get_type.return_value = DataTest.test_ingredient_type
    mock_ingredient.get_price.return_value = DataTest.test_ingredient_price
    return mock_ingredient




@pytest.fixture(scope='function')
def create_ingredient_second():
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = DataTest.test_ingredient_name_2
    mock_ingredient.get_type.return_value = DataTest.test_ingredient_type_2
    mock_ingredient.get_price.return_value = DataTest.test_ingredient_price
    return mock_ingredient

