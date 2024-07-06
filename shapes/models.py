from django.db import models

class Shape(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    color = models.CharField(max_length=7)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Suggestion(models.Model):
    text = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:1000]  
