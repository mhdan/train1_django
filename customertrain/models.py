from django.db import models


# this class is separate from others and others are main!!!
class Customers(models.Model):
    ID = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=20)
    AGE = models.IntegerField()
    ADDRESS = models.CharField(max_length=25, default=None,
                               null=True, blank=True)
    SALARY = models.DecimalField(max_digits=18, decimal_places=2,
                                 null=True, blank=True, default=None)
# this class is separate from others and others are main!!!


class Clients(models.Model):
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=50)


class Manufacturers(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=300)


class Products(models.Model):
    manufacturer = models.ForeignKey(Manufacturers, on_delete=models.CASCADE)
    name_of_product = models.CharField(max_length=100)
    cost_per_item = models.DecimalField(max_digits=18, decimal_places=2)


class Client_Orders(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products)
    order_no = models.AutoField(primary_key=True)
    fulfill_by_date = models.DateField(null=True, blank=True, default=None)
