from django.contrib import admin

from birthday_app.models import Employee


# Registers the Models so the admin can make changes.
admin.site.register(Employee)
