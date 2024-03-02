
import pytest

pytestmark = pytest.mark.django_db

class TestCategoryModel:
    #Arrange
    def test_str_method(self, category_factory):
    #Act
        x = category_factory(name="test_cat")
    #Assert
        x.__str__() == "test_category"

class TestBrandModel:
    pass


class TestProductModel:
    pass