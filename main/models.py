from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)

class Person(models.Model):
    SHIRT_SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large')
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
