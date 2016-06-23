from django.contrib import admin

from .models import Employee, Birthdate


# Registers the Models so the admin can make changes.
admin.site.register(Employee)
admin.site.register(Birthdate)
