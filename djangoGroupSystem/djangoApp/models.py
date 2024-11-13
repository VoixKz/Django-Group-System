from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.core.exceptions import ValidationError
from datetime import date


def validate_birth_date(value):
    if value > date.today():
        raise ValidationError('Дата рождения не может быть в будущем')
    if value < date(1900, 1, 1):
        raise ValidationError('Дата рождения не может быть ранее 1 января 1900 года')
    

class Group(models.Model):
    name = models.CharField(
        max_length=100, 
        unique=True,
        verbose_name="Название группы",
        validators=[RegexValidator(regex=r'^SEP-\d{3}\.\d$', message='Название группы должно быть в формате SEP-XXX.X')]
    )
    level = models.PositiveIntegerField(
        verbose_name="Уровень группы",
        validators=[MinValueValidator(1, message='Уровень группы должен быть не менее 1'), MaxValueValidator(4, message='Уровень группы должен быть не более 4')]
    )
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class Student(models.Model):
    first_name = models.CharField(
        max_length=100, 
        verbose_name="Имя",
        validators=[RegexValidator(regex=r'^[A-Z][a-z]+$', message='Имя должно начинаться с заглавной буквы и содержать только буквы')]
    )
    last_name = models.CharField(
        max_length=100, 
        verbose_name="Фамилия",
        validators=[RegexValidator(regex=r'^[A-Z][a-z]+$', message='Фамилия должна начинаться с заглавной буквы и содержать только буквы')]
    )
    birth_date = models.DateField(
        verbose_name="Дата рождения",
        validators=[validate_birth_date]
    )
    group_id = models.ForeignKey(Group, on_delete=models.SET_NULL, verbose_name="Группа", related_name="students", null=True)
    avg_mark = models.DecimalField(
        verbose_name="Средний балл", 
        decimal_places=2, 
        max_digits=4,
        validators=[MinValueValidator(0, message='Средний балл должен быть не менее 0'), MaxValueValidator(10, message='Средний балл должен быть не более 10')]
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"