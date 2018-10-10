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
    city = models.CharField(max_length=24)
    street = models.CharField(max_length=32)
    house_no = models.SmallIntegerField()  # na później: rozstrzygnąć kwestię numerów np. 15c
    flat_no = models.SmallIntegerField(null=True)
    resident = models.ForeignKey(Person, on_delete=models.DO_NOTHING)


class PhoneNumber(models.Model):

    number = models.CharField(max_length=15)
    category = models.SmallIntegerField(choices=CATEGORIES)
    owner = models.ForeignKey(Person, on_delete=models.DO_NOTHING)


class EmailAddress(models.Model):
    address = models.CharField(max_length=32)
    category = models.SmallIntegerField(choices=CATEGORIES)
    owner = models.ForeignKey(Person, on_delete=models.DO_NOTHING)


class Group(models.Model):
    name = models.CharField(max_length=15)
    member = models.ManyToManyField(Person)
