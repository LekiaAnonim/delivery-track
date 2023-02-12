from django.contrib import admin
from .models import Package
# Register your models here.
admin.site.register(Package)


class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'track_id', 'receive_date', 'owner',
                    'destination_address', 'country', 'arrival_date', 'delivery_status', 'comment')
    fields = ['name', 'short_description', 'track_id', 'receive_date',
              'owner', 'destination_address', 'country', 'arrival_date', 'delivery_status', 'comment']
    


class ProductInline(admin.TabularInline):
    model = PackageAdmin
