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
    address = models.ForeignKey('Address', on_delete=models.CASCADE, null=True)
    phones = models.ForeignKey('PhoneNumber', on_delete=models.CASCADE, null=True)
    emails = models.ForeignKey('EmailAddress', on_delete=models.CASCADE, null=True)
    groups = models.ManyToManyField('Group')


class Address(models.Model):
    city = models.CharField(max_length=24, default='')
    street = models.CharField(max_length=32, default='')
    house_no = models.CharField(max_length=5, default='')  # na później: rozstrzygnąć kwestię numerów np. 15c
    # flat_no = models.CharField(max_length=5, default='')



class PhoneNumber(models.Model):

    number = models.CharField(max_length=20, default='')
    category = models.SmallIntegerField(choices=CATEGORIES, default=1)


    def __str__(self):
        return self.number

class EmailAddress(models.Model):
    address = models.CharField(max_length=32, default='')
    category = models.SmallIntegerField(choices=CATEGORIES, default=1)



class Group(models.Model):
    name = models.CharField(max_length=16)


    def __str__(self):
        return self.name