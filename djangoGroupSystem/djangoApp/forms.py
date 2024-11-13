from django import forms
from .models import Student, Group

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'birth_date', 'avg_mark', 'group_id']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'avg_mark': forms.NumberInput(attrs={'class': 'form-control'}),
            'group_id': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'birth_date': 'Дата рождения',
            'avg_mark': 'Средний балл',
            'group_id': 'Группа',
        }


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'level', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control formDescription'}),
        }
        labels = {
            'name': 'Название группы',
            'level': 'Уровень группы',
            'description': 'Описание',
        }