# Create your models here.
"""
- Each model is represented by a class that subclasses django.db.models.Model. 
- Each model has a number of class variables, each of which represents a database field in the model.

With this info, Django is able to:

1) Create a database schema (CREATE TABLE statements) for this app.
2) Create a Python database-access API for accessing Recipe and Category objects.

"""

import datetime
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(u'Name', max_length=50)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = u'Category'
        verbose_name_plural = u'Categories'

    # this gives us a more helpful representation of this object in the interactive Python shell
    # also because objects’ representations are used throughout Django’s automatically-generated admin.
    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(u'Title', max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ManyToManyField(Category, verbose_name=u'Categories')
    ingredients = models.TextField(
        u'Ingredients', help_text=u'One ingredient per line')
    preparation = models.TextField(u'Preparation')
    pub_date = models.DateField(
        'date published', default=timezone.now)

    class Meta:
        verbose_name = u'Recipe'
        verbose_name_plural = u'Recipes'
        # ordering = ['-pub_date']

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
