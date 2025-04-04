from rest_framework import serializers
from .models import Company
from .models import Employee


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
     
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.company_name', read_only=True)

    class Meta:
        model = Employee
        fields = [
            'id', 'employee_name', 'employee_id', 'current_role', 'department',
            'start_date', 'left_date', 'duties', 'company', 'company_name'
        ]
