from django.urls import path
from . import views

urlpatterns = [

    path('clickhouse/', views.clickhouse_view, name='clickhouse_view'),

]
