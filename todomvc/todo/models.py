from django.db import models

# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    order models.PositiveSmallIntegerField(null=True, blank=True)
