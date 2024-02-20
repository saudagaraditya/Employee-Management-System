"""
URL configuration for CRM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from employee.views import login_view, reset_password_view,index,add_product,view_product_page,dashboard,add_doctor,schedule_appointment,today_schedule,deals_detail,logout_view,about,edit_product,delete_product


urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('reset_password/', reset_password_view, name='reset_password'),
    path('add_product/', add_product, name='add_product'),
    path('view_product_page/', view_product_page, name='view_product_page'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add_doctor/', add_doctor, name='add_doctor'),
    path('schedule-appointment/', schedule_appointment, name='schedule_appointment'),
    path('today-schedule/',today_schedule, name='today_schedule'),
    path('deals-detail/', deals_detail, name='deals_detail'),
    path('about/', about, name='about'),
    path('products/<int:product_id>/edit/', edit_product, name='edit_product'),
    path('products/<int:product_id>/delete/', delete_product, name='delete_product'),

]
if settings:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)