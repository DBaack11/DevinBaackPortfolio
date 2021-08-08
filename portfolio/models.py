from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    video = models.FileField(upload_to='portfolio/videos')
    github = models.URLField(blank=True)
    tools = models.CharField(max_length=200)
    writeUp = models.TextField()

    def __str__(self):
        return self.title

