from django.db import models

# Create your models here. 

class Location(models.Model):
    name = models.CharField(max_length=100, unique = True)

    def __str__(self):
        return self.name

class Event(models.Model):
    date = models.DateField("date published")
    time = models.TimeField("time published")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    county = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.date} | {self.time} | {self.county} | {self.occupation} | {self.description[:200]}"

