from django.db import models

# Create your models here.

class Empolye(models.Model):
    emp_id=models.IntegerField()
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    salary=models.IntegerField()

    def __str__(self):
        return self.name
