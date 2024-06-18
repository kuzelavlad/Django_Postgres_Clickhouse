from django.shortcuts import render
from rest_framework.response import Response
from users.clickhouse_models import ClickHouseUsers


def clickhouse_view(request):
    # Set a valid id value within the UInt32 range
    new_user = ClickHouseUsers(id=1, name="users", value=42)
    new_user.save(using='clickhouse')

    users = ClickHouseUsers.objects.using('clickhouse').all()
    return render(request, 'users/clickhouse.html', {'users': users})