from django.contrib import admin
from django.utils.html import format_html
from .models import Employee,Product,Doctor,Appointment,DealsDetail

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'date_of_joining', 'status']
    
    

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialisation', 'contact','entered_by']
    list_filter = ['entered_by']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'company_name', 'img_display','price','entered_by']
    list_filter = ['entered_by']

    def img_display(self, obj):
        return format_html('<img src="{}" width="90" height="90"/>', obj.image.url)

    img_display.short_description = 'Image'

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'date', 'time','entered_by']
    list_filter = ['entered_by']

class DealsDetailsAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'product', 'quantity_ordered','entered_by']
    list_filter = ['entered_by']




# Register your models here.

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Appointment,AppointmentAdmin)
admin.site.register(DealsDetail,DealsDetailsAdmin)









