from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import PatientIntake, SOAPNote, ClinicMetrics
from django.utils import timezone


def home(request):
    # Get the latest metrics entry
    metrics = ClinicMetrics.objects.order_by('-date').first()

    context = {
        'metrics': metrics
    }
    return render(request, 'core/home.html', context)


def patient_intake(request):
    if request.method == 'POST':
        form = PatientIntakeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core/thank_you.html')
    else:
        form = PatientIntakeForm()
    return render(request, 'core/patient_intake.html', {'form': form})

def physician_dashboard(request):
    patients = PatientIntake.objects.all()
    selected_patient = None
    soap_notes = []
    dashboard_metrics = {}

    if request.method == "POST" or request.GET.get("patient"):
        patient_id = request.POST.get('patient') or request.GET.get('patient')
        if patient_id:
            selected_patient = get_object_or_404(PatientIntake, pk=patient_id)
            soap_notes = SOAPNote.objects.filter(patient=selected_patient).order_by('-created_at')

            # Patient dashboard metrics
            num_visits = soap_notes.count()
            most_recent_visit = soap_notes.first().created_at if num_visits > 0 else None

            # Average time between visits
            if num_visits > 1:
                dates = list(soap_notes.values_list('created_at', flat=True))
                dates.sort()
                deltas = [(dates[i+1] - dates[i]).days for i in range(len(dates)-1)]
                avg_days_between_visits = sum(deltas) / len(deltas)
            else:
                avg_days_between_visits = None

            dashboard_metrics = {
                'num_visits': num_visits,
                'most_recent_visit': most_recent_visit,
                'avg_days_between_visits': avg_days_between_visits,
            }

    return render(request, 'core/physician_dashboard.html', {
        'patients': patients,
        'selected_patient': selected_patient,
        'soap_notes': soap_notes,
        'dashboard_metrics': dashboard_metrics,
    })