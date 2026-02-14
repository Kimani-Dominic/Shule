from django.urls import path
from .views import *

urlpatterns = [
    path('api/students/create', CreateStudentView.as_view(), name='create_student'),
    path('api/students', StudentListView.as_view(), name='get_students'), 
    path('api/students/<int:pk>', StudentDetailView.as_view(), name='get_student'),
    path('api/students/<int:pk>/update', UpdateStudentView.as_view(), name='update_student'),
    path('api/students/<int:pk>/delete', DeleteStudentView.as_view(), name='delete_student'),
]