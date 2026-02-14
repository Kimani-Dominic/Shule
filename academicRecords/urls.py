from django.urls import path
from . import views

urlpatterns = [
    path('api/academic-records', views.AcademicRecordListCreateView.as_view(), name='record-list'),
    path('api/academic-records/<int:pk>', views.AcademicRecordDetailView.as_view(), name='record-detail'),
]