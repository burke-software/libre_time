from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    organization = models.ForeignKey('orgs.Organization')

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.name


class Entry(models.Model):
    task = models.ForeignKey(Task)
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    delta = models.DurationField(blank=True, null=True)

    def __str__(self):
        return 'Started {} at {}'.format(self.task, self.start)
