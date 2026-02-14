from django.db import models

class Cart(models.Model):
    created_at              = models.DateTimeField(auto_now_add = True)
    updated_at              = models.DateTimeField(auto_now = True)
    finished_at             = models.DateTimeField(default = True)
    def __str__(self):
        return f"Carrinho #{self.id}"