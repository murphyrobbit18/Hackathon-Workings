import os, sys
import django
import random
from datetime import timedelta, date
from faker import Faker

# Point Django to your settings module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_project.settings')
django.setup()

from core.models import PatientIntake, SOAPNote
from django.contrib.auth.models import User

fake = Faker()

# ------------------------------
# Step 1: Create physician users
# ------------------------------
def create_physicians():
    physicians = []
    # List of usernames/emails for fake physicians
    users_info = [
        ('dr_smith', 'dr_smith@example.com'),
        ('dr_jones', 'dr_jones@example.com'),
        ('dr_lee', 'dr_lee@example.com')
    ]

    for username, email in users_info:
        user, created = User.objects.get_or_create(username=username, defaults={
            'email': email,
        })
        if created:
            user.set_password('password123')  # default password
            user.is_staff = True
            user.save()
            print(f"Created physician user: {username}")
        else:
            print(f"Physician {username} already exists")
        physicians.append(user)

    return physicians

# ------------------------------
# Step 2: Create fake patients
# ------------------------------
def create_fake_patients(num_patients=5, physicians=[]):
    for _ in range(num_patients):
        patient = PatientIntake.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            dob=fake.date_of_birth(minimum_age=0, maximum_age=90),
            contact_number=fake.phone_number(),
            symptoms=fake.sentence(nb_words=6)
        )
        print(f"Created patient: {patient}")

        # Create 3 previous SOAP notes
        for i in range(3):
            past_date = date.today() - timedelta(days=random.randint(10, 180))
            physician_assigned = random.choice(physicians)
            SOAPNote.objects.create(
                patient=patient,
                physician=physician_assigned,
                subjective=fake.sentence(nb_words=10),
                objective=fake.sentence(nb_words=10),
                assessment=fake.sentence(nb_words=8),
                plan=fake.sentence(nb_words=6),
                created_at=past_date
            )
        print(f"  Added 3 previous SOAP notes for {patient}")

# ------------------------------
# Main execution
# ------------------------------
if __name__ == "__main__":
    physicians = create_physicians()
    create_fake_patients(num_patients=10, physicians=physicians)
    print("Fake data population complete!")