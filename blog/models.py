from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField


# This is the blog apps database
# each class resembles a table
# each variable within class resembles a column
class Post(models.Model):
    title = models.CharField(max_length=120, default='Title')
    author = models.CharField(max_length=55, default='Author')
    slug = AutoSlugField(populate_from='title', unique=True)

    body = models.TextField()
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    # def _get_unique_slug(self):
    #     slug = slugify(self.title)
    #     unique_slug = slug
    #     num = 1
    #     while Post.objects.filter(slug=unique_slug).exists():
    #         unique_slug = '{}-{}'.format(slug, num)
    #         num += 1
    #     return unique_slug
    #
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = self._get_unique_slug()
    #     super().save()

