from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import bank2
import csv

from .serilizers import BankSerilizer, BankSerilizer2


def homepage(request):

    return HttpResponse("credixco")

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'

class BankListView(generics.ListCreateAPIView):

    serializer_class = BankSerilizer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self, *args, **kwargs):
        queryset = bank2.objects.all()
        ifsc = self.request.GET.get('ifsc')
        if ifsc:
            queryset= queryset.filter(ifsc=ifsc)

        return queryset

class BankListView_branch(generics.ListCreateAPIView):

    serializer_class = BankSerilizer2
    pagination_class = StandardResultsSetPagination

    def get_queryset(self, *args, **kwargs):
        queryset = bank2.objects.all()
        city = self.request.GET.get('city')
        bank1 = self.request.GET.get('bank')
        queryset=queryset.filter( Q(city__icontains=city)|Q(bank_name__icontains=bank1))

        return queryset
