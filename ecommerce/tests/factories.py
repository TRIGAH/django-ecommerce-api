
import factory

from product.models import Brand, Category, Product


class CategotyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "test_category"    