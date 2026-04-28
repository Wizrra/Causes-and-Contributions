import site

from django.contrib import admin

from api_app.models import Causes, Contribute

# Register your models here.
# admin.site.register(Causes)
# admin.site.register(Contribute)

@admin.register(Causes)
class CausesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at')

@admin.register(Contribute)
class ContributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'amount', 'causes', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at', 'causes')