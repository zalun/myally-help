from django.contrib import admin

from .models import Cause

class CauseAdmin(admin.ModelAdmin):
        prepopulated_fields = {"slug": ("name",)}


admin.site.register(Cause, CauseAdmin)
