from rest_framework import serializers

from company.models import Employee, Department


class EmployeeModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class DepartmentModelSerializer(serializers.ModelSerializer):
    employees_count = serializers.IntegerField(read_only=True)
    full_salary = serializers.DecimalField(read_only=True, max_digits=18, decimal_places=2)

    class Meta:
        model = Department
        fields = [
            'name',
            'director',
            'employees_count',
            'full_salary'
        ]
