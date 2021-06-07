from cms.plugin_pool import plugin_pool
from cmsplugin_cascade.bootstrap4.plugin_base import BootstrapPluginBase
from cmsplugin_cascade.plugin_base import CascadePluginBase


class PricingProductsPlugin(BootstrapPluginBase):
    name = 'Product Price Table'
    render_template = 'shop/catalog/pricing_planset.html'


plugin_pool.register_plugin(PricingProductsPlugin)
