from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
import django_filters.rest_framework
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
# Create your views here.
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from .models import *
from .serializers import ProductSerializer


@api_view(['GET'])
def getAllProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getAllCategory(request):
    cat = Category.objects.all()
    serializer = CategorySerializer(cat, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCategory(request, pk):
    products = SubCategory.objects.all()
    products = products.filter(itemId_id = pk)
    serializer = SubCategorySerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAllSubCategory(request):
    products = SubCategory.objects.all()
    serializer = SubCategorySerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPopularProducts(request):
    products = Product.objects.all()
    products = products.filter(id__in=[7, 1, 8, 13])
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def getAllOrders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

class OrderSet(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

@api_view(['GET'])
def getCart(request, pk):
    cart = Cart.objects.get(_id=pk)
    serializer = CartSerializer(cart, many=False)
    return Response(serializer.data)


class CartSet(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

@api_view(['GET'])
def getProductsBySort(request, s):
    products = Product.objects.all().order_by(f'{s}')
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProductsBySortDown(request, s):
    products = Product.objects.all().order_by(f'-{s}')
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProductBySubcategory(request, pk):
    products = Product.objects.all()
    products = products.filter(category_id=pk)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

class ProductListSearch(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Product.objects.filter(purchaser=user)


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    #filterset_fields = ['title']
    search_fields = ('title',)
