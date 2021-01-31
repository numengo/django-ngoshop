# -*- coding: utf-8 -*-
"""
Created on Thu Aug 06 12:46:34 2015

@author: Cedric
"""
import logging
import time
from ngomm.transforms import Freeplane2InstanceTransform
from django.core.management.base import BaseCommand

from ngomm.models import Map
from ngomm_cms.models import Page
from ...repositories import ProductRepository, ProductPageRepository
from ...models.nodes import ProductNode, ProductPageNode


class Command(BaseCommand):
    help = 'update shop catalog from django-app mindmap'
    args = ""

    def add_arguments(self, parser):
        parser.add_argument(
            'filepath',
            nargs='?',
        )

    def handle(self, filepath, *args, **options):
        from django.conf import settings
        #languages = [l['code'] for l in settings.CMS_LANGUAGES[1]]
        languages = ['en']
        map = Map.load_from_file(filepath)
        mm_page = Page(node=map.node)
        products = map.node.get_descendant('Shop', 'products')
        if products:
            repo = ProductRepository()
            for n in products.node_visible:
                mm_product = ProductNode(node=n)
                repo.create_or_update_db(mm_product)
        catalogs = map.node.get_descendant('Shop', 'catalogs')
        if catalogs:
            repo = ProductPageRepository()
            for n in products.node_visible:
                mm_catalog = ProductPageNode(node=n)
                repo.create_or_update_db(mm_catalog)
        assert mm_page

