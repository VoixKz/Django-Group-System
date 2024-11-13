from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Group
from .forms import StudentForm, GroupForm
from django.db.models import Count, Avg, Max


def home(request):
    return render(request, 'home.html')


def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GroupForm()

    context = {
        'form': form,
    }
    return render(request, 'create_group.html', context)


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()

    context = {
        'form': form,
    }
    return render(request, 'create_student.html', context)


def maintain_system(request):
    groups = Group.objects.annotate(
        students_count=Count('students'),
        average_score=Avg('students__avg_mark'),
        best_score=Max('students__avg_mark')
    )

    context = {
        'groups': groups,
    }
    return render(request, 'maintain_system.html', context)


def maintain_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    students = group.students.all()

    context = {
        'group': group,
        'students': students,
    }
    return render(request, 'maintain_group.html', context)