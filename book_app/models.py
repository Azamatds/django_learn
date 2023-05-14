from django.db import models
from django.utils.text import slugify
from transliterate import translit


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=70)
    rating = models.IntegerField()
    is_best_selling = models.BooleanField()
    author = models.CharField(max_length=100, null=True)
    slug = models.SlugField(default='', name=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}-{self.rating}'


class FeedBack(models.Model):
    name = models.CharField(max_length=70)
    surname = models.CharField(max_length=70)
    feedback = models.CharField(max_length=70)


