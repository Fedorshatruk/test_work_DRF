from django.core.exceptions import ValidationError


def validate_director(value):
    from company.models import Employee
    if not Employee.objects.filter(id=value, position=Employee.DIRECTOR).exists():
        raise ValidationError('Сотрудник не является директором')
