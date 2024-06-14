from django.contrib import admin
from .models import Personal, Manager, Worker


@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ['type']
    # list_filter = ('type_of_user', 'currency')
    # search_fields = ('type_of_user')


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'email', 'phone', 'address')
    list_filter = ('type', 'currency')
    search_fields = ('name', 'email', 'phone')


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'email', 'phone', 'address')
