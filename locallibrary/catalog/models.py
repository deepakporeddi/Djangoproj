from django.db import models

class Collection(models.Model):
    title=models.CharField(max_length=255)
    def __str__(self):
        return self.title

class Promotions(models.Model):
    description=models.TextField(null=True)
    discount=models.FloatField()
