from clickhouse_connect import Client


def get_clickhouse_client():
    return Client(host='clickhouse', port=8123)
