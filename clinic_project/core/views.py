from django.shortcuts import render, redirect
from .forms import PatientIntakeForm

def home(request):
    return render(request, 'core/home.html')


def patient_intake(request):
    if request.method == 'POST':
        form = PatientIntakeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core/thank_you.html')
    else:
        form = PatientIntakeForm()
    return render(request, 'core/patient_intake.html', {'form': form})
