from django.core.exceptions import ValidationError
from django.db import models

from company.validators import validate_director


class Employee(models.Model):
    CLERK = 1
    MANAGER = 2
    DIRECTOR = 3

    POSITION = (
        (CLERK, 'Служащий'),
        (MANAGER, 'Менеджер'),
        (DIRECTOR, 'Директор')
    )

    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255, db_index=True)
    middle_name = models.CharField(verbose_name='Отчество', max_length=255)
    position = models.PositiveSmallIntegerField(choices=POSITION, verbose_name='Должность')
    salary = models.DecimalField(verbose_name='Оклад', max_digits=15, decimal_places=2)
    department = models.ForeignKey(
        'company.Department',
        verbose_name='Департамент',
        on_delete=models.CASCADE,
        related_name='employees'
    )
    photo = models.ImageField(verbose_name='Фото')

    class Meta:
        verbose_name = 'Сотрудник',
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.position}'

    def full_clean(self, exclude=None, validate_unique=True):
        return super(Employee, self).full_clean()

    def validate_unique(self, **kwargs):
        super(Employee, self).validate_unique(**kwargs)
        if self.position == self.DIRECTOR and self.department.director:
            raise ValidationError('У департамента есть директор, сотрудник не может стать директором')


class Department(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    director = models.OneToOneField(
        Employee,
        verbose_name='Директор',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        validators=[validate_director],
        related_name='director'
    )

    class Meta:
        verbose_name = 'Департамент',
        verbose_name_plural = 'Департамент'

    def __str__(self):
        return f'{self.name}'