from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from .models import Employee,Product,Doctor,Appointment
from .forms import ProductForm,DoctorForm,AppointmentForm,DealsDetailForm
from django.contrib.auth import logout
from django.contrib import messages



# Create your views here.


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        employee = Employee.objects.filter(email=email, password=password, status='active').first()
        if employee is not None:
            return render(request, 'dashboard.html', {'employee': employee})
        else:
            error_message = 'Invalid email or password'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return render(request,'login.html')  


def reset_password_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            employee = Employee.objects.get(email=email, status='active')
            success_message = 'Password reset instructions sent to your email'
            return render(request, 'reset_password.html', {'success_message': success_message})
        except Employee.DoesNotExist:
            error_message = 'Invalid email'
            return render(request, 'reset_password.html', {'error_message': error_message})
    return render(request, 'reset_password.html')


    
def index(request):
    if request.method == 'GET':

     return render(request, 'index.html')
    
def about(request):
    if request.method == 'GET':

     return render(request, 'about.html')
    


def dashboard(request):
    total_products = Product.objects.count()
    
    return render(request, 'dashboard.html',{'total_products': total_products})

   

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            messages.success(request, 'Product Added successfully!')
            return redirect('add_product')  
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})



def view_product_page(request):
    products = Product.objects.all()
    return render(request, 'view_product_page.html', {'products': products})


def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.company_name = request.POST.get('company_name')
        product.price = request.POST.get('price')
        product.save()
        messages.success(request, 'Product Saved successfully!')


    return render(request, 'edit_product.html', {'product': product})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('view_product_page')
    
    return render(request, 'delete_product.html', {'product': product})



def add_doctor(request):
    form = DoctorForm()  
    
    
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.save()
            messages.success(request, 'Doctor Added successfully!')
            return redirect('add_doctor')
        
    else:
        form = DoctorForm()
    
    return render(request, 'add_doctor.html', {'form': form})

def schedule_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)  
        if form.is_valid():  
            appointment = form.save(commit=False)
            appointment.date = form.cleaned_data['schedule_date'] 
            appointment.time = form.cleaned_data['schedule_time']
            appointment.save()  
            messages.success(request, 'Appointment Schedulled successfully!')
            return redirect('schedule_appointment')   
    else:
        form = AppointmentForm()  
    appointments = Appointment.objects.all()
    return render(request, 'schedule_appointment.html', {'form': form})

def today_schedule(request):
    
    if request.method == 'POST':
        date = request.POST.get('date')
        appointments = Appointment.objects.filter(date=date)
        context = {'appointments': appointments}
        return render(request, 'today_schedule.html', context)
    
    return render(request, 'date_selector.html')

    

def deals_detail(request):
    if request.method == 'POST':
        form = DealsDetailForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Deal Added Successfully')
            return redirect('deals_detail')
    else:
        form = DealsDetailForm()
    
    return render(request, 'deals_detail.html', {'form': form})




def appointment_chart(request):
    doctors = Doctor.objects.all()
    data = []

    for doctor in doctors:
        appointments = Appointment.objects.filter(doctor=doctor)
        data.append({
            'doctor_name': doctor.name,
            'appointment_count': appointments.count()
        })

    return render(request, 'appointment_chart.html', {'data': data})




    

