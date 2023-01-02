from urllib import response
from django import views
from .models import *
from .serializers import *

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.db.models import Q

class CustomPagination(PageNumberPagination):
    '''
    Here i used this pagination to fetch list of datas so using this pagination the API will be scalable we can load 1 lakh datas
    without server slow
    '''
    page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'navigate':{
                'next_page' : self.get_next_link(),
                'previous_page':self.get_previous_link()
            },
            'page_count' : self.page.paginator.count,
            'current_page' : self.page.number,
            'result' : data
        })




class ProductList(ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    search_fields = ['product_name','category']

    product = None
    def get_queryset(self,*args, **kwargs):
        
        '''
        Here using this 'product_name' and 'category' we can search particular data
        '''
        # filter using amount
        
            
        # filter using product name    
        if 'product_name' in self.request.GET.keys(): 
            prd_data = self.request.GET['product_name'] #if self.request.GET('product_name', False) else self.request.GET('search', False)
            product = Product.objects.filter(slug=prd_data)
        
        # filter using category name    
        elif 'category' in self.request.GET.keys():
            cat_data = self.request.GET['category']
            product = Product.objects.select_related('category').filter(category__slug=cat_data)
        
        elif 'start_amount' in self.request.GET.keys() or 'end_amount' in self.request.GET.keys():
            print("coming")
            start_amount = int(self.request.GET['start_amount'])
            end_amount = int(self.request.GET['end_amount'])
            product = Product.objects.filter(product_price__gte=start_amount).filter(product_price__lte=end_amount)
        
        else:
            product = Product.objects.select_related('category').all() 
        print("product ",product)
        return product
