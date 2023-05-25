from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'


# added ni nimo


class Reply(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='replies')
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"Reply by {self.author.username} on {self.article.title}"


# if ever mag make kag new models
# python manage.py makemigrations
# python manage.py migrate
