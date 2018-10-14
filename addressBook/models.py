from django.db import models

# Create your models here.

CATEGORIES = (
    (1, 'prywatny'),
    (2, 'domowy'),
    (3, 'służbowy'),
    (4, 'secret'),
)


class Person(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=42, default='')
    description = models.TextField(default='')


class Address(models.Model):
    city = models.CharField(max_length=24, default='')
    street = models.CharField(max_length=32, default='')
    house_no = models.CharField(max_length=5, default='')  # na później: rozstrzygnąć kwestię numerów np. 15c
    flat_no = models.CharField(max_length=5, default='')
    resident = models.ForeignKey(Person, on_delete=models.CASCADE)


class PhoneNumber(models.Model):

    number = models.CharField(max_length=20, default='')
    category = models.SmallIntegerField(choices=CATEGORIES, default=1)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)


class EmailAddress(models.Model):
    address = models.CharField(max_length=32, default='')
    category = models.SmallIntegerField(choices=CATEGORIES, default=1)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField(max_length=16)
    member = models.ManyToManyField(Person)
