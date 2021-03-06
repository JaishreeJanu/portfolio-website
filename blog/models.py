from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=20)


class Post(models.Model):

    title = models.CharField(max_length=255)

    body = RichTextUploadingField(blank=True, config_name='special')

    description = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)

    last_modified = models.DateTimeField(auto_now=True)

    categories = models.ManyToManyField('Category', related_name='posts')


    def __str__(self):
        return self.title

class Comment(models.Model):

    author = models.CharField(max_length=60)

    body = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('Post', on_delete=models.CASCADE)
