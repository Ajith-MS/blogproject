from django.db import models

class Dishes(models.Model):
    name=models.CharField(max_length=200,unique=True)
    category=models.CharField(max_length=200)
    price=models.PositiveIntegerField()

    def __str__(self):
        return self.name