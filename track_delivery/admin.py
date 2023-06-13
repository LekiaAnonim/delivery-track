from django.contrib import admin
from .models import Package
# Register your models here.
admin.site.register(Package)


class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'track_id', 'owner', 'phone_number', 'current_location',
                    'destination_address', 'country', 'arrival_date', 'delivery_status', 'comment')
    fields = ['name', 'short_description', 'track_id',
              'receiver','sender', 'phone_number', 'current_location', 'destination_address', 'country', 'arrival_date', 'delivery_status', 'comment']


class ProductInline(admin.TabularInline):
    model = PackageAdmin
