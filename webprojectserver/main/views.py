from rest_framework import viewsets, status

from .models import Category, DiscountCode, Product, ShoppingCart
from .serializers import (
    CategorySerializer,
    DiscountCodeSerializer,
    ProductSerializer,
    ShoppingCartSerializer,
    UserRegistrationSerializer,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DiscountCodeViewSet(viewsets.ModelViewSet):
    queryset = DiscountCode.objects.all()
    serializer_class = DiscountCodeSerializer


class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer

class UserRegistrationAPIView(APIView):
    permission_classes = []
    authentication_classes = []
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "Login successful"})
        else:
            return Response({"error": "Invalid Credentials"}, status=401)
        

class CheckAuthView(APIView):

    def get(self, request):
        return Response({"username": request.user.username, "is_authenticated": True})
