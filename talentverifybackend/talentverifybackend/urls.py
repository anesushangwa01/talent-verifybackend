"""
URL configuration for talentverifybackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from talentverify.views import add_company, add_employee, get_companies, list_employees , update_employee,employee_detail,update_company,get_company,delete_company

urlpatterns = [
    path('admin/', admin.site.urls),
   path('add-company/', add_company, name='add-company'),
   path('companies/', get_companies, name='get_companies'),
   path('companies/<int:pk>/update/', update_company, name='update_company'),
   path('companies/<int:pk>/', get_company, name='get_company'),
   path('companies/<int:pk>/delete/', delete_company, name='delete_company'),





   path('add-employee/', add_employee, name='add-employee'),
   path('employees/', list_employees, name='list_employees'),
   path('employees/<int:pk>/', employee_detail, name='employee_detail'),
   path('employees/<int:pk>/update/', update_employee, name='update_employee'),

]
