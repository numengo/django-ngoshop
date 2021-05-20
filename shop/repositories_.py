# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

from io import BytesIO
from future.utils import with_metaclass
from ngoschema.protocols import ObjectProtocol, SchemaMetaclass
from ngoschema.registries import repositories_registry

from ngocms.repositories import ImageRepository, PageRepository
from django.core.files import File as DjangoFile

from ngoutils.models import DjangoModelNodeAbstractBase
from ngoutils.repositories import django_model_node_repository_registry, DjangoModelNodeRepository

from ngomm.models import InstanceNode

from .models.defaults.commodity import Commodity
from .models.product import BaseProduct, BaseProductManager
from .models.inventory import BaseInventory, AvailableProductMixin
from .models.defaults.order import Order
from .models.defaults.mapping import ProductPage, ProductImage
from .models.defaults.customer import Customer
from .models.notification import Notification, NotificationAttachment

from .models.product import BaseProduct
from .models.related import BaseProductPage, BaseProductImage
from .models.nodes import ProductPageNode, ProductNode, ProductImageNode


@django_model_node_repository_registry.register()
class ProductRepository(with_metaclass(SchemaMetaclass, DjangoModelNodeRepository)):
    _django_model_node = ProductNode

    def __init__(self, *args, **kwargs):
        DjangoModelNodeRepository.__init__(self, *args, **kwargs)
        self._image_repo = ProductImageRepository()

    def create_or_update_db(self, product, parent_db=None):
        pass


@django_model_node_repository_registry.register()
class ProductPageRepository(with_metaclass(SchemaMetaclass, PageRepository)):
    _django_model_node = ProductPageNode

    def __init__(self, *args, **kwargs):
        PageRepository.__init__(self, *args, **kwargs)
        self._product_repo = ProductRepository()
        self._page_repo = PageRepository()

    def create_or_update_db(self, page, parent_db=None):
        pass


@django_model_node_repository_registry.register()
class ProductImageRepository(with_metaclass(SchemaMetaclass, ImageRepository)):
    _django_model_node = ProductImageNode

    def __init__(self, *args, **kwargs):
        ImageRepository.__init__(self, *args, **kwargs)

    def create_or_update_db(self, pr, parent_db=None):
        pass
