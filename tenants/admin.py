from django.contrib import admin
from .models import Tenant

class TenantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Tenant, TenantAdmin)