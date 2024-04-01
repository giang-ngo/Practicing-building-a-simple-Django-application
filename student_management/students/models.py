from django.db import models
from .db_connection import db

student_collection = db['Student']


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    class_name = models.CharField(max_length=50)
    average_score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.full_name
