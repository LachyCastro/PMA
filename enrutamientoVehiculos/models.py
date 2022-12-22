from django.db import models

# Create your models here.

class Publication(models.Model):
    name = models.CharField(max_length=30)
    path = models.CharField(max_length=200)
    autor = models.CharField(max_length=200, blank=True, null= True)
    solutions_method = models.CharField(max_length=200, blank=True, null= True)

    def __str__(self) -> str:
        return self.name