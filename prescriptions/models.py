from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    person_id = models.CharField(max_length=11)  # Assuming Turkish ID format
    # Add other patient details
    # Patient Model: Contains fields for patient details.
    def __str__(self):
        return self.full_name

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other medicine details
    # Medicine Model: Contains fields for medicine details.
    def __str__(self):
        return self.name

class Pharmacy(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other pharmacy details
    # Pharmacy Model: Utilizes Django's built-in 'User' model for authentication and stores additional details specific to pharmacies.

class Prescription(models.Model):
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicines = models.ManyToManyField(Medicine)
    # Add other prescription details
    # Prescription Model: Relates pharmacies, patients, and medicines through foreign keys and many-to-many relationships.
    def __str__(self):
        return f"{self.patient.full_name}'s Prescription"

