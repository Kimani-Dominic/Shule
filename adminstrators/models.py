from django.db import models

# Create your models here.
class Administrator(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=20, blank=True)
    employee_id = models.CharField(max_length=20, unique=True)
    # role = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    class Meta:
        permissions = [
            ("add_academic_records", "Can add academic records to students"),
            ("change_academic_records", "Can update academic records"),
        ]