from django.db import models


class Profile(models.Model):
    user = models.OneToOneField('auth.User', primary_key=True)

    def __str__(self):
        return str(self.user)


class Organization(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(Profile, blank=True)

    def __str__(self):
        return self.name
