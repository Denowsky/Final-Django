from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.category_name

class Ingredient(models.Model):
    ing_name = models.CharField(max_length=50)
    kcal = models.IntegerField()
    def __str__(self) -> str:
        return self.ing_name

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    steps = models.TextField()
    time = models.TimeField()
    image = models.ImageField(default='default.jpg')
    author = models.CharField(max_length=100)
    ingredient = models.ManyToManyField(Ingredient)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=16)
