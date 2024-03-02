
import pytest

pytestmark = pytest.mark.django_db

class TestCategoryModel:
    #Arrange
    def test_str_method(self, category_factory):
    #Act
        x = category_factory(name="test_cat")
    #Assert
        x.__str__() == "test_cat"

class TestBrandModel:
    #Arrange
    def test_str_method(self, brand_factory):
    #Act
        x = brand_factory(name="test_brand")
    #Assert
        x.__str__() == "test_brand"


class TestProductModel:
    pass