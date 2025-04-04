from django.urls import path
from .views import create_company
from .views import add_employee
from .views import get_companies,employee_list_api

urlpatterns = [
    path("create/", create_company, name="create_company"),
    path("create/", add_employee, name="create_employee"),
    path('companies/', get_companies, name='get_companies'),  
      path('employees/', employee_list_api, name='employee_list_api')# Ensure this line is added for getting companies
    
     
]
