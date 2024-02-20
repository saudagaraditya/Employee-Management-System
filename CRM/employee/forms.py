from django import forms
from .models import Product,Doctor,Appointment,DealsDetail,Employee
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone



class ProductForm(forms.ModelForm):
    entered_by = forms.ModelChoiceField(queryset=Employee.objects.all())
    class Meta:
        model = Product
        fields = ['name', 'company_name', 'image', 'price', 'entered_by']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price == 0:
            raise forms.ValidationError('price must be greater than zero.')
        return price 

class DoctorForm(forms.ModelForm):
    entered_by = forms.ModelChoiceField(queryset=Employee.objects.all())
    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        if len(str(contact)) != 10 :
            raise forms.ValidationError('Enter Valid contact number')
        return contact

    class Meta:
        model = Doctor
        fields = ['name', 'specialisation', 'contact', 'location', 'entered_by']

User = get_user_model()

class AppointmentForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all().order_by('name'))
    schedule_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=datetime.date.today
    )

    def clean_schedule_date(self):
        schedule_date = self.cleaned_data.get('schedule_date')
        if schedule_date < timezone.now().date():
            raise forms.ValidationError('Selected date must be today or a future date.')
        return schedule_date
    
    schedule_time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        initial=datetime.datetime.now().strftime('%H:%M')
    )
    
    entered_by = forms.ModelChoiceField(queryset=Employee.objects.all())

    class Meta:
        model = Appointment
        fields = ['doctor', 'schedule_date', 'schedule_time', 'entered_by']


class DealsDetailForm(forms.ModelForm):
    class Meta:
        model = DealsDetail
        fields = ['doctor', 'product', 'quantity_ordered', 'entered_by']

    def clean_quantity_ordered(self):
        quantity_ordered = self.cleaned_data.get('quantity_ordered')
        if quantity_ordered == 0:
            raise forms.ValidationError('Quantity must be greater than zero.')
        return quantity_ordered        
