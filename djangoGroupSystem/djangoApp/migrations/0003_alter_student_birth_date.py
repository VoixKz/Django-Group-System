# Generated by Django 5.1.3 on 2024-11-13 15:48

import djangoApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoApp', '0002_alter_group_level_alter_group_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birth_date',
            field=models.DateField(validators=[djangoApp.models.validate_birth_date], verbose_name='Дата рождения'),
        ),
    ]
