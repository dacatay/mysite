from django.db import models


# This is the blog apps database
# each class resembles a table
# each variable within class resembles a column
class Post(models.Model):
    title = models.CharField(max_length=255, default='Title')
    author = models.CharField(max_length=55, default='Author')
    slug = models.SlugField(default='Slug')

    body = models.TextField()
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.title



