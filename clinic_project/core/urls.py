from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('intake/', views.patient_intake, name='patient_intake'),
    # Add more pages here as needed
]
