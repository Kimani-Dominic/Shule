from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'middle_name', 'last_name', 'email', 'phonenumber', 'enrollment_date', 'academic_records']
        read_only_fields = ['enrollment_date', 'academic_records', 'id']
        
        
        
        


