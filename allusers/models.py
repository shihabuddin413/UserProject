from django.db import models

# Create your models here.


class SingleUser (models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    carrerIndustry = models.CharField(max_length=200)

    def __str__(self):
        return self.name
