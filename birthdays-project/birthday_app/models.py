from django.db import models


class Birthdate(models.Model):
    date_of_birth = models.DateField()

    # Displays date in a dd-MMM-yy format.
    def __str__(self):
        return self.date_of_birth.strftime('%d %b %y')  # pragma: no cover


# Creates a Person Model.
class Employee(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='First Name')
    last_name = models.CharField(max_length=30, verbose_name='Last Name')
    date_of_birth = models.ForeignKey(Birthdate, editable=True,
                                      verbose_name='Date of Birth')

    # Presents users by first and last name in the description.
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)  # pragma: no cover
