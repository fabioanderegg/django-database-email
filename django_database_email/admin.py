from django.contrib import admin

from apps.email.models import EMail


@admin.register(EMail)
class EMailAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')
