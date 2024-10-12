from django.shortcuts import render, get_object_or_404, redirect


def index_page(request):
    return render(request, 'pages/index.html')

def home_page(request):
    return render(request, 'pages/home.html')

def about_page(request):
    return render(request, 'pages/about.html')

def login_page(request):
    return render(request, 'pages/login.html')


from django.shortcuts import render, get_object_or_404, redirect
from .models import Doctor, Patient, Appointment, Prescription, MedicalRecord
from .forms import DoctorForm, PatientForm, AppointmentForm, PrescriptionForm, MedicalRecordForm

# Doctor Views
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'pages/doctor_list.html', {'doctors': doctors})

def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'pages/doctor_detail.html', {'doctor': doctor})

def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'pages/doctor_form.html', {'form': form})

def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'pages/doctor_form.html', {'form': form})

def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'pages/doctor_confirm_delete.html', {'doctor': doctor})

# Repeat similar views for Patient, Appointment, Prescription, and MedicalRecord models
