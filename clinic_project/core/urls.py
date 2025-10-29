from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('intake/', views.patient_intake, name='patient_intake'),
    path('dashboard/', views.physician_dashboard, name='physician_dashboard'),
    # Add more pages here as needed
]
