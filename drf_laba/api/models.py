from django.db import models


class Group(models.Model):
    GroupNAMES = [
        ('admin', 'admin'),
        ('Cook', 'cook'),
        ('Waiter', 'waiter'),

    ]

    name = models.CharField(max_length=50, choices=GroupNAMES)

    def __str__(self):
        return self.name

class Employee(models.Model):

    STATUS = [
        ('In work', 'in work'),
        ('Not in work', 'not in work')
    ]
    name = models.CharField(max_length=200)
    login = models.CharField(max_length=400)
    status = models.CharField(max_length=200, choices=STATUS)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):

    STATUS = [
        ('отменен', 'cancel'),
        ('оплачен', 'paid'),
        ('готовится', 'inCook'),
        ('готов', 'ready')
    ]

    table = models.IntegerField()
    employees = models.ForeignKey(Employee, on_delete=models.CASCADE)
    time = models.TimeField()
    fullprice = models.IntegerField()
    status = models.CharField(max_length=200, choices=STATUS)
    positions = models.ManyToManyField(Products)


class Shift(models.Model):
    shiftStart = models.TimeField()
    shiftEnd = models.TimeField()
    orders = models.ManyToManyField(Order)
    employees = models.ManyToManyField(Employee)


