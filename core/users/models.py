from django.db import models


# Django==3.2.12

class Personal(models.Model):
    TYPES_OF_ADMINISTRATION = (
        ("A", "High Level"),
        ("B", "Mid Level"),
        ("C", "Low Level"),
    )
    type = models.CharField(verbose_name='Type of user', max_length=50, choices=TYPES_OF_ADMINISTRATION)

    class Meta:
        verbose_name = 'Personal'
        verbose_name_plural = 'Personal'


class Manager(Personal):
    CURRENCY_CHOICES = (
        ("EUR", "Euro"),
        ("USD", "USD"),
        ("BTC", "BTC"),
    )

    name = models.CharField(verbose_name='Name', max_length=50)
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(verbose_name='Phone', max_length=50)
    address = models.CharField(verbose_name='Address', max_length=50)
    currency = models.CharField(verbose_name='Currency', max_length=50, choices=CURRENCY_CHOICES)
    salary = models.DecimalField(verbose_name='Salary', decimal_places=2, max_digits=10)

    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'

    def __str__(self):
        return f'{self.name}\n {self.type}'


class Worker(Manager):
    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'

    def __str__(self):
        return f'{self.name}\n {self.type}'
