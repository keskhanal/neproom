from django.contrib import admin

from .models import Staff

class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Staff, StaffAdmin)
