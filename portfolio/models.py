from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='portfolio/images/')
    date = models.DateTimeField(auto_now=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title[:50]
