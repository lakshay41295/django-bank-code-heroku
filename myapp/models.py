from django.db import models


class bank2 (models.Model):
    ifsc=models.CharField(max_length=500)
    bank_id=models.CharField(max_length=500)
    branch=models.CharField(max_length=500)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=500)
    district=models.CharField(max_length=500)
    state=models.CharField(max_length=500)
    bank_name=models.CharField(max_length=500)