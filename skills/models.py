from django.db import models

# Create your models here.

class SkillsModel(models.Model):
    skill = models.CharField(max_length=50)
    measure = models.PositiveIntegerField()

    class Meta:
       ordering = ['-measure']
