from django.apps import AppConfig


class ProductModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product_module'
    verbose_name = 'محصول'
    verbose_name_plural = 'محصولات'
