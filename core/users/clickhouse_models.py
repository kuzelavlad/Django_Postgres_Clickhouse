from django.db import models


class ClickHouseUsers(models.Model):
    id = models.PositiveIntegerField(primary_key=True)  # Use PositiveIntegerField for unsigned integers
    name = models.CharField(max_length=255)
    value = models.IntegerField()

    class Meta:
        managed = False
        app_label = 'users'
        db_table = 'users_table'
