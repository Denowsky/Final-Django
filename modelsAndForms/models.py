from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50)

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    kcal = models.IntegerField(max_length=10)

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    steps = models.TextField()
    time = models.TimeField()
    image = models.ImageField()
    author = models.CharField(max_length=100)
    ingredient = models.ManyToManyField(Ingredient)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=16)
