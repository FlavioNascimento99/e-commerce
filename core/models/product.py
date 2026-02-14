from django.db import models


class Product(models.Model):
    product_name            = models.CharField(max_length = 100)
    product_price           = models.DecimalField(max_digits = 10, decimal_places = 2)
    product_brand           = models.CharField(max_length = 64)
    product_description     = models.TextField(max_length = 450)
    product_stock           = models.DecimalField(max_digits = 3)
    product_is_active       = models.BooleanField(default = True)
    product_created_at      = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return f"Produto de id: #{self.id}"