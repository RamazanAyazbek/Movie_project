from django.contrib import admin
from .models import Contact
# admin.site.register(Contact)
@admin.register(Contact)
class ConatctAdmin(admin.ModelAdmin):
    list_display=("email", "date")