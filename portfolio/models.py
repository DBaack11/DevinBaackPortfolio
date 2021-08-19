from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    video = models.URLField(blank=True)
    image = models.URLField(blank=True)
    github = models.URLField(blank=True)
    tools = models.CharField(max_length=200)
    writeUp = models.TextField()

    def __str__(self):
        return self.title

