
from product.models import Brand, Category, Product


class CategotyFactory():
    class Meta:
        model = Category

    name = "test_category"    