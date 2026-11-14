from django.db import models

# Create your models here.
class Foodlog(models.Model):

    title = models.CharField(max_length=200)

    calorie = models.PositiveIntegerField()

    MEAL_TYPE_CHOICES = (
        ("breakfast","breakfast"),
        ("lunch","lunch"),
        ("dinner","dinner"),
        ("snacks","snacks"),
    )

    meal_type = models.CharField(max_length=200,choices=MEAL_TYPE_CHOICES)

    serving_size = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    owner = models.CharField(max_length=200)

    def __str__(self):
        
        return self.title