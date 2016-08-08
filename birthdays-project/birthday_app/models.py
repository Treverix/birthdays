from django.db import models


# Creates a Person Model.
class Employee(models.Model):
    # This class does something
    first_name = models.CharField(max_length=20, verbose_name='First Name')
    last_name = models.CharField(max_length=30, verbose_name='Last Name')
    date_of_birth = models.DateField(verbose_name='Birthdate')

    # Presents users by first and last name in the description.
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)  # pragma: no cover
