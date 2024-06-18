from django.db import models
from django.utils import timezone


class BaseDateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Personal(models.Model):
    type = models.CharField(verbose_name='Type of personal', max_length=50)

    class Meta:
        verbose_name = 'Personal'
        verbose_name_plural = 'Personal'

    def __str__(self):
        return self.type


class Manager(models.Model):
    CURRENCY_CHOICES = (
        ("EUR", "Euro"),
        ("USD", "USD"),
        ("BTC", "BTC"),
    )

    type = models.ForeignKey(
        Personal,
        on_delete=models.CASCADE,
        verbose_name='Type of personal'
    )

    name = models.CharField(verbose_name='Name', max_length=50)
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(verbose_name='Phone', max_length=50)
    address = models.CharField(verbose_name='Address', max_length=50)
    position = models.CharField(verbose_name='Position', max_length=50)
    salary = models.DecimalField(verbose_name='Salary', decimal_places=2, max_digits=10)
    currency = models.CharField(verbose_name='Currency', max_length=50, choices=CURRENCY_CHOICES)

    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'

    def __str__(self):
        return f'{self.name}\n {self.type}'


class Worker(models.Model):
    CURRENCY_CHOICES = (
        ("EUR", "Euro"),
        ("USD", "USD"),
        ("BTC", "BTC"),
    )
    type = models.ForeignKey(
        Personal,
        on_delete=models.CASCADE,
        verbose_name='Type'
    )

    name = models.CharField(verbose_name='Name', max_length=50)
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(verbose_name='Phone', max_length=50)
    address = models.CharField(verbose_name='Address', max_length=50)
    position = models.CharField(verbose_name='Position', max_length=50)
    salary = models.DecimalField(verbose_name='Salary', decimal_places=2, max_digits=10)
    currency = models.CharField(verbose_name='Currency', max_length=50, choices=CURRENCY_CHOICES)

    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'

    def __str__(self):
        return f'{self.name}\n {self.type}'
