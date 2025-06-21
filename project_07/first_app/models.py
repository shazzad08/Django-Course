from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    fathers_name = models.TextField(default="Sajid")
     

    def __str__(self):       #  database er obj er name change krar jnno use krte hoy
        return f"Roll: {self.roll} Name: {self.name}"