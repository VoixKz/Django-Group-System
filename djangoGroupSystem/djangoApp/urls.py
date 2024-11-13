from django.urls import path
from .views import home, create_group, create_student, maintain_system, maintain_group


urlpatterns = [
    path('', home, name='home'),
    path('create_group/', create_group, name='create_group'),
    path('create_student/', create_student, name='create_student'),
    path('maintain_system/', maintain_system, name='maintain_system'),
    path('maintain_group/<int:group_id>/', maintain_group, name='maintain_group'),
]