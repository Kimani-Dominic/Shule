from rest_framework import serializers
from .models import *

class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = ['id', 'first_name', 'middle_name', 'last_name', 'email', 'phonenumber', 'employee_id']
        read_only_fields = ['id']