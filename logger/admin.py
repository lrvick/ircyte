from django.contrib import admin
from logger.models import Log

class LogAdmin(admin.ModelAdmin):
    list_display = ('nick', 'id', 'type', 'created')

admin.site.register(Log, LogAdmin)
