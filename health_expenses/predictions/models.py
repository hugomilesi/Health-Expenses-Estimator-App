from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# predictions/models.py

class Prediction(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=1)
    sex = models.CharField(max_length=6)
    age = models.IntegerField()
    region = models.CharField(max_length=20)
    children = models.IntegerField()
    smoker = models.CharField(max_length=3)
    bmi = models.FloatField()
    predicted_cost = models.FloatField()

    def __str__(self):
        return f"{self.sex} | {self.age} | {self.region} | {self.predicted_cost}"
