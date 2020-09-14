from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True, upload_to='project_images/')
    code = models.URLField()
    detail = RichTextField()

    def __str__(self):
        return self.title