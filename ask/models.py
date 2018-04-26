from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateTimeField()


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    count = models.IntegerField(default=0)


class Like(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('author', 'article'),)
