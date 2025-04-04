from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Company,Employee
from .serializers import CompanySerializer,EmployeeSerializer
# from .serializers import EmployeeSerializer

@api_view(['POST'])
def add_company(request):
    if request.method == 'POST':
        print("Incoming data:", request.data)  # 👈 Check the structure of incoming JSON
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("Validation errors:", serializer.errors)  # 👈 Shows what went wrong
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

@api_view(['POST'])
def add_employee(request):
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
def get_companies(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)



# get all employees in the company
@api_view(['GET'])
def list_employees(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)