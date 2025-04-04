from django.db import models


# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    register_number = models.CharField(max_length=100, unique=True)
    register_date = models.DateField()
    company_address = models.TextField()
    contact_person = models.CharField(max_length=255)
    number_of_employees = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    departments = models.TextField(help_text="Comma separated list of departments")
    
    def __str__(self):
        return self.company_name


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="employees")
    employee_name = models.CharField(max_length=255)
    employee_id = models.CharField(max_length=50, unique=True)
    current_role = models.CharField(max_length=255)
    department = models.CharField(max_length=100)
    start_date = models.DateField()
    left_date = models.DateField(null=True, blank=True)
    duties = models.TextField(blank=True, null=True)

 
    def __str__(self):
        return f"{self.employee_name} - {self.company.company_name}"
