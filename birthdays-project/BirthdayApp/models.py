from django.db import models


# Creates a user Model.
class User(models.Model):
    firstName = models.TextField(max_length=20)
    lastName = models.TextField(max_length=30)

    # Presents users by first and last name in the description.
    def __str__(self):
        return "%s %s" % (self.firstName, self.lastName)
