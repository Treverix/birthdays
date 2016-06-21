from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

# Register your models here.
from .models import User


# Modifies the appearance of the textfields in the admin section.
class ModAdmin(admin.ModelAdmin):
    formfield_overrides = {
        # Changes the default appearance of the admin backend so the
        # boxes are more reasonably sized.
        models.TextField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }

# Registers the User Model so the admin can make changes.
admin.site.register(User, ModAdmin)
