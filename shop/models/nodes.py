# -*- coding: utf-8 -*-

from django.db import models

from ngomm.models import InstanceNode
from ngoutils.models import DjangoModelNodeAbstractBase

from .product import BaseProduct
from .related import BaseProductPage, BaseProductImage

ProductNode = InstanceNode.make_class_from_model_uri('https://numengo.org/django#/$defs/my_big_bang_shop/$defs/Product', 'ProductNode')
ProductPageNode = InstanceNode.make_class_from_model_uri('https://numengo.org/django#/$defs/my_big_bang_shop/$defs/ProductPage', 'ProductPageNode')
ProductImageNode = InstanceNode.make_class_from_model_uri('https://numengo.org/django#/$defs/my_big_bang_shop/$defs/ProductImage', 'ProductImageNode')


class DjangoProductNode(DjangoModelNodeAbstractBase):
    _object_node = ProductNode
    _django_model = BaseProduct
    product = models.ForeignKey(BaseProduct, on_delete=models.CASCADE)


class DjangoProductPageNode(DjangoModelNodeAbstractBase):
    _object_node = ProductPageNode
    _django_model = BaseProductPage
    product_page = models.ForeignKey(BaseProductPage, on_delete=models.CASCADE)


class DjangoProductImageNode(DjangoModelNodeAbstractBase):
    _object_node = ProductImageNode
    _django_model = BaseProductImage
    product_image = models.ForeignKey(BaseProductImage, on_delete=models.CASCADE)
