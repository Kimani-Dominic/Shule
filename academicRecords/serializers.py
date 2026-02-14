from rest_framework import serializers
from .models import AcademicRecord
from students.models import Student

class AcademicRecordSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.full_name', read_only=True)
    student_email = serializers.EmailField(source='student.email', read_only=True)
    graded_by_name = serializers.CharField(source='graded_by.__str__', read_only=True)
    
    class Meta:
        model = AcademicRecord
        fields = [
            'id', 
            'student', 
            'student_name', 
            'student_email', 
            'course_name', 
            'grade', 
            'graded_by',
            'graded_by_name'
        ]
        extra_kwargs = {
            'student': {'write_only': True},
            'graded_by': {'write_only': True, 'required': False, 'allow_null': True}
        }

class StudentSerializer(serializers.ModelSerializer):
    academic_records = AcademicRecordSerializer(many=True, read_only=True)
    full_name = serializers.CharField(read_only=True)
    
    class Meta:
        model = Student
        fields = [
            'id', 
            'first_name', 
            'middle_name', 
            'last_name', 
            'full_name', 
            'email', 
            'phonenumber', 
            'enrollment_date', 
            'academic_records'
        ]