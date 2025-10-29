import os
import sys
import django
import random
from datetime import timedelta, date
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Point Django to your settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_project.settings')

django.setup()

from core.models import ClinicMetrics

def populate_metrics(days=10):
    today = date.today()
    for i in range(days):
        day = today - timedelta(days=i)
        total_patients = random.randint(30, 80)
        avg_wait = round(random.uniform(10.0, 45.0), 1)
        appointments = random.randint(20, 60)
        staff = random.randint(5, 12)

        ClinicMetrics.objects.create(
            date=day,
            total_patients_seen=total_patients,
            avg_wait_time_minutes=avg_wait,
            appointments_today=appointments,
            staff_on_duty=staff
        )
        print(f" Added metrics for {day}: {total_patients} patients, avg {avg_wait} min wait")

if __name__ == '__main__':
    populate_metrics()
