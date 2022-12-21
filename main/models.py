from django.db import models
from django.utils.text import slugify
# Create your models here.


class Reservations(models.Model):
    name = models.CharField(default= 'None', max_length=30)
    Restaurant = models.ForeignKey("Restaurant", on_delete=models.PROTECT)
    Booking_time = models.DateTimeField(null=False, blank=False, unique=True)
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Table(models.Model):
    restaurant = models.ForeignKey("Restaurant", on_delete=models.PROTECT)
    table_number = models.CharField(max_length=2, default="0")
    def __str__(self):
        return self.table_number

class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    people = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='meals/')
    slug = models.SlugField(blank=True, null=True)


def save(self, *args, **kwargs):
    if not self.slug and self.name:
        self.slug = slugify(self.name)
    super(Meals, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'meal'
        verbose_name_plural = 'meals'


def __str__(self):
    return self.name
