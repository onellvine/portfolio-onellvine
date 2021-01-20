from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.CharField(max_length=512, help_text="separate tags by commas", blank=True)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    