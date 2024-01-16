from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Patient, Medicine, Pharmacy, Prescription
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@login_required
def create_prescription(request):
    # Your logic for creating prescriptions
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        person_id = request.POST.get('person_id')
        medicine_name = request.POST.get('medicine_name')
        medicine_price = request.POST.get('medicine_price')

        if not all([patient_name, person_id, medicine_name, medicine_price]):
            return HttpResponse("Please provide all necessary fields.")

        try:
            patient, patient_created = Patient.objects.get_or_create(full_name=patient_name, person_id=person_id)
            medicine, medicine_created = Medicine.objects.get_or_create(name=medicine_name, price=medicine_price)
            pharmacy = Pharmacy.objects.get(user=request.user)

            prescription, prescription_created = Prescription.objects.get_or_create(pharmacy=pharmacy, patient=patient)
            prescription.medicines.add(medicine)

            return redirect('view-prescription', prescription_id=prescription.id)
        except Exception as e:
            return HttpResponse(f"Error creating prescription: {e}")
    else:
        return render(request, 'create_prescription.html')

@login_required
def view_prescription(request, prescription_id):
    prescription = get_object_or_404(Prescription, id=prescription_id)
    # Fetch patient name and medicines
    patient_name = prescription.patient.full_name
    medicines = ', '.join([medicine.name for medicine in prescription.medicines.all()])
    return render(request, 'view_prescription.html', {'prescription': prescription, 'patient_name': patient_name, 'medicines': medicines})
# Define other views as per your requirements...


@login_required
def logout_view(request):
    logout(request)
    return redirect('base-prescriptions')  # home URL

def base_prescriptions(request):
    #"username: busrasu password:busra123"
    return HttpResponse("Welcome to the Prescriptions app")
    
def get_patient_name(request, person_id):
    # Simüle edilmiş bir API çağrısı sonucunda ismi al
    # Gerçek uygulamada bu bilgi veritabanından alınmalıdır
    patients = {
        '12345678910': 'John Doe',
        '98765432100': 'Jane Doe',
        
    }
    patient_name = patients.get(person_id, 'Patient not found')
    return JsonResponse({'name': patient_name})

class MedicineListAPIView(APIView):
    def get(self, request):
        # Bu kısma ilaç listesini çekme kodunu ekleyin
        medication_names = ["ASPIRIN", "CASPOBIEM", "CASPOPOL", "CORASPIN", "SIGMASPORIN", "VASPARIN"]

        response_data = {"medicationNames": medication_names}
        return Response(response_data, status=status.HTTP_200_OK)