"""
    User Model

"""
from django.db import models


class User(models.Model):
    user_name               = models.CharField(max_length = 120)
    user_email              = models.CharField(max_length = 64)
    user_password           = models.CharField(max_length = 100)
    def __str__(self):
        return f"Usuário #{self.user_name} de E-mail #{self.user_email}"
