from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=20, blank=True)
    enrollment_date = models.DateField(auto_now_add=True)
    academic_records = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"  
    