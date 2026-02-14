from django.db import models
from adminstrators.models import Administrator
from students.models import Student

class AcademicRecord(models.Model):
    student = models.ForeignKey(
        Student, 
        on_delete=models.CASCADE, 
        related_name='student_grades'
    )
    course_name = models.CharField(max_length=100)
    grade = models.CharField(max_length=2)
    graded_by = models.ForeignKey(
        Administrator,
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )

    def __str__(self):
        return f"{self.student.full_name} - {self.course_name}: {self.grade}"
    
    @property
    def student_name(self):
        return self.student.full_name
    
    @property
    def student_email(self):
        return self.student.email