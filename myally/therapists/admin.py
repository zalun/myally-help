from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Therapist

# Use the Therapist inside the User account
class TherapistInline(admin.StackedInline):
    model = Therapist
    can_delete = False
    verbose_name_plural = "Therapist"
    fk_name = "user"


class TherapistAdmin(UserAdmin):
    inlines = (TherapistInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(TherapistAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, TherapistAdmin)
