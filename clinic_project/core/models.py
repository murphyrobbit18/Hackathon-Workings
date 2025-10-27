from django.db import models
from django.contrib.auth.models import User

class PatientIntake(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    contact_number = models.CharField(max_length=15, blank=True)
    symptoms = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    reviewed_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class SOAPNote(models.Model):
    patient = models.ForeignKey(PatientIntake, on_delete=models.CASCADE)
    physician = models.ForeignKey(User, on_delete=models.CASCADE)
    subjective = models.TextField()
    objective = models.TextField()
    assessment = models.TextField()
    plan = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SOAP Note for {self.patient} by {self.physician}"
