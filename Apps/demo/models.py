from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Book(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=150, null=True, blank=False, unique=True)
    description = models.TextField(verbose_name=_('Description'), max_length=125, blank=True)
    rating = models.DecimalField(verbose_name=_('Price'), default=0, decimal_places=2, max_digits=5)
    published = models.DateField(verbose_name=_('Publish Date'), blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(verbose_name=_('Image'), upload_to='covers/', blank=True)