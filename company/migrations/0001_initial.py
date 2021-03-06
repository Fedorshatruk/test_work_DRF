# Generated by Django 4.0.3 on 2022-04-06 09:59

import company.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(db_index=True, max_length=255, verbose_name='Фамилия')),
                ('middle_name', models.CharField(max_length=255, verbose_name='Отчество')),
                ('position', models.PositiveSmallIntegerField(choices=[(1, 'Служащий'), (2, 'Менеджер'), (3, 'Директор')], verbose_name='Должность')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Оклад')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фото')),
                ('department', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='company.department', verbose_name='Департамент')),
            ],
            options={
                'verbose_name': ('Сотрудник',),
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='director',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='director', to='company.employee', validators=[company.validators.validate_director], verbose_name='Директор'),
        ),
    ]
