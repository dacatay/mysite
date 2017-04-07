from django.db import models


# This is the blog apps database
# each class resembles a table
# each variable within class resembles a column
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField()

    # metadata
    def __str__(self):
        return self.title
