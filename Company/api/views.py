from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Company.models import Company
from Account.api.serializers import UserSerializer
from Account.models import User
from .serializers import CompanySerializer

@api_view(['GET','POST'])
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            first_name = serializer.validated_data['manager_first_name']
            last_name = serializer.validated_data['manager_last_name']
            email = serializer.validated_data['manager_email']
            password = serializer.validated_data['manager_password']

            user = User.objects.create(first_name = first_name,last_name=last_name,email=email,username = email,password=password)

            serializer.validated_data['company_manager'] = user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def company_detail(request, pk):
    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)