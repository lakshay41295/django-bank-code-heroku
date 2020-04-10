from rest_framework import serializers
from .models import bank2



class BankSerilizer(serializers.ModelSerializer):
    class Meta:
         model=bank2
         fields=('ifsc','branch','address','city','district','state', 'bank_name','bank_id')

class BankSerilizer2(serializers.ModelSerializer):
    class Meta:
         model=bank2
         fields=('branch',)