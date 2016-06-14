from django.db import models


class User(models.Model):
    firstName = models.TextField(max_length=20)
    lastName = models.TextField(max_length=30)

    def __str__(self):
        return "%s %s" % (self.firstName, self.lastName)
