from django.db import models
from django.utils.text import slugify
# Create your models here.


class Meals(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    people = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='meals/')
    slug = models.SlugField(blan=True, null=True)


def save(self, *args, **kwargs):
    if not self.slug and self.name:
        self.slug = slugify(self.name)
    super(Meals, self).save(*args, **kwargs)


def __str__(self):
    return self.name
