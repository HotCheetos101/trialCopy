from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    # add in thumbnail
    # add in author

    # needs to be indentend

    def __str__(self):
        return self.title

    def snipper(self):
        return self.body[:50] + '...'


# if ever mag make kag new models
# python manage.py makemigrations
# python manage.py migrate
