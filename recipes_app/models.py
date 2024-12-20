from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    steps = models.TextField()
    cooking_time = models.IntegerField(help_text="Введите время в минутах")
    image = models.ImageField(upload_to='recipes_images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
