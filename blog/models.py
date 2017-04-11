from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField


# This is the blog apps database
# each class resembles a table
# each variable within class resembles a column
class Post(models.Model):
    title = models.CharField(max_length=120, default='Title')
    author = models.CharField(max_length=55, default='Author')
    slug = AutoSlugField(populate_from='title', unique=True)

    body = HTMLField()
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.title


