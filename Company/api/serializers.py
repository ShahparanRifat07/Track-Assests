from rest_framework import serializers
from Company.models import Company
from Account.api.serializers import UserSerializer

class CompanySerializer(serializers.ModelSerializer):
    company_manager = UserSerializer()

    manager_first_name = serializers.CharField(source='company_manager.first_name',write_only=True)
    manager_last_name = serializers.CharField(source='company_manager.last_name',write_only=True)
    manager_email = serializers.EmailField(source='company_manager.email',write_only=True)
    manager_password = serializers.CharField(source='company_manager.password',write_only=True)

    class Meta:
        model = Company
        fields = ['id','manager_first_name','manager_last_name','manager_email', 'manager_password','company_name', 'company_email',
                   'company_manager', 'stripe_product_id', 'premium',
                  'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at','premium','stripe_product_id']
        depth = 1
