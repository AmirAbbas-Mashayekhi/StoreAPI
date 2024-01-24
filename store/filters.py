from django_filters.rest_framework import FilterSet

from store.models import Product


# Look at the docs for `django-filter`
class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'collection_id': ['exact'],
            'unit_price': ['gt', 'lt'],
        }
