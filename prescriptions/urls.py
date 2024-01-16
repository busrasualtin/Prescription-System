from django.urls import path
from . import views
from .views import MedicineListAPIView


urlpatterns = [
    path('', views.base_prescriptions, name='base-prescriptions'),
    path('create/', views.create_prescription, name='create-prescription'),
    path('<int:prescription_id>/', views.view_prescription, name='view-prescription'),
    path('logout/', views.logout_view, name='logout'),  # Add logout URL
    path('api/get_patient_name/<str:person_id>/', views.get_patient_name, name='get_patient_name'),
    path('api/medicines/', MedicineListAPIView.as_view(), name='medicine-list'),
    # Other URL patterns...
]