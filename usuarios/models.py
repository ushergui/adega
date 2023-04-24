from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('ADMIN', 'Admin'),
        ('GERENTE', 'Gerente'),
        ('FUNCIONARIO', 'Funcionário'),
    )

    user_type = models.CharField(max_length=17, choices=USER_TYPES, default='FUNCIONARIO',verbose_name="Perfil de usuário")
