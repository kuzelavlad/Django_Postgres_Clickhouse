from django.contrib import admin
from .models import Personal, Manager, Worker


@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ['type']


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'phone', 'position')
    list_filter = ['type']
    search_fields = ['name']


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'phone', 'position')
    list_filter = ['type']
    search_fields = ['name']
