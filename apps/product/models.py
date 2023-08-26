from django.db import models

from utils.choices import PetStatusChoices
from utils.models import BaseModel, SlugModel
from apps.file.models import Image


# Create your models here.


class Tag(SlugModel):
    name = models.CharField(max_length=255, verbose_name='Название тега')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name[:10] or self.name


class Category(SlugModel):
    name = models.CharField(max_length=255,
                            unique=True,
                            verbose_name='Название категории')
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               null=True, blank=True,
                               verbose_name='Родительская категория')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name[:20] or self.name


class Pet(SlugModel):
    name = models.CharField(max_length=255,
                            verbose_name='Имя питомца')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='category_pet',
                                 null=True, blank=True,
                                 verbose_name='Категория')
    # photoUrls = models.ImageField(upload_to='pet_photos',
    #                               verbose_name='Фото питомца')
    photoUrls = models.ManyToManyField(Image,
                                       blank=True,
                                       related_name='photoUrls_pet',
                                       verbose_name='Фото питомца')

    tags = models.ManyToManyField(Tag,
                                  blank=True,
                                  related_name='tags_pet',
                                  verbose_name='Теги')
    status = models.CharField(max_length=26,
                              choices=PetStatusChoices.choices,
                              default=PetStatusChoices.AVAILABLE,
                              verbose_name='Статус питомца')

    class Meta:
        verbose_name = 'Домашний питомец'
        verbose_name_plural = 'Домашний питомец'

    def __str__(self):
        return self.name[:10] or self.name
