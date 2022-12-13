from django.db import models

# Create your models here.


def jls_extract_def(max_length, max_digits, decimal_places, upload_to):
    class Meals(models.Model):
        name = models.CharField(max_length=50)
        description = models.TextField(max_length=500)
        people = models.IntegerField()
        price = models.DecimalField(max_digits=5, decimal_places=2)
        image = models.ImageField(upload_to='meals/')    return image


image = jls_extract_def(max_length, max_digits, decimal_places, upload_to)

