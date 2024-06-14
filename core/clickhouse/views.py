from django.shortcuts import render
from .clickhouse import get_clickhouse_client


def clickhouse_example(request):
    client = get_clickhouse_client()
    result = client.query('SELECT * FROM your_table')
    return render(request, 'your_template.html', {'result': result})
