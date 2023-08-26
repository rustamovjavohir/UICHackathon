from django.db import models
from utils.models import BaseModel, SlugModel
from apps.product.models import Pet


# Create your models here.

class Order(SlugModel):
    name = models.CharField(max_length=255, verbose_name='Название тега')
    STATUS = (
        ('placed', 'placed'),
        ('approved', ' approved'),
        ('delivered', 'delivered'),
    )
    petId = models.ForeignKey(Pet, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=1000, decimal_places=2)
    shipDate = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS, default='available')
    complete = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name[:10] or self.name


class Address(SlugModel):
    street = models.CharField(max_length=150, )
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.street[:10] or self.street
