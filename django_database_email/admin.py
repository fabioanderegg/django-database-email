from django.contrib import admin

from .models import EMail


@admin.register(EMail)
class EMailAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')
