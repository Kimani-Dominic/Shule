from django.urls import path
from .views import *

urlpatterns = [
    path('api/administrators/create', CreateAdministratorView.as_view(), name='create_administrator'),
    path('api/administrators', AdministratorListView.as_view(), name='get_administrators'), 
    path('api/administrators/<int:pk>', AdministratorDetailView.as_view(), name='get_administrator'),
    path('api/administrators/<int:pk>/update', UpdateAdministratorView.as_view(), name='update_administrator'),
]