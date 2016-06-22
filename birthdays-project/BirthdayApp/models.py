from django.db import models


class Birthdate(models.Model):
    dob = models.DateField(max_length=8)

    # Displays date in a dd-MMM-yy format.
    def __str__(self):
        return '{:%d %b %y}'.format(self.dob)


# Creates a user Model.
class User(models.Model):
    firstName = models.TextField(max_length=20, verbose_name='First Name')
    lastName = models.TextField(max_length=30, verbose_name='Last Name')
    dob = models.ForeignKey(Birthdate, editable=True, max_length=8,
                            verbose_name='Date of Birth')

    # Presents users by first and last name in the description.
    def __str__(self):
        return "%s %s" % (self.firstName, self.lastName)
