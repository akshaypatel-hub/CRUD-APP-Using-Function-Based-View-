from django.db import models

# Create your models here.


class Employee(models.Model):
    Name = models.CharField(max_length=100)
    Salary = models.FloatField()
    Address = models.CharField(max_length=200)

    def __str__(self):
        return self.Name
