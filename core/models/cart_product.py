from django.db import models

class CartProduct(models.Model):
    cart = models.ForeignKey(
        Cart,
        related_name = 'Items',
        on_delete = models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete = models.CASCADE
    )

    quantity   = models.PositiveBigIntegerField(default = 1)
    unit_price = models.DecimalField(max_digits = 10, decimal_places = 2)
    def subtotal(self): 
        return f"Quantidade de produtos: #{self.quantity} | Preço unitário: #{self.unit_price} : Total: f{self.quantity * self.unit_price}"