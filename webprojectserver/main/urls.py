from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet,
    DiscountCodeViewSet,
    ProductViewSet,
    ShoppingCartViewSet,
    UserRegistrationAPIView,
    LoginView,
    CheckAuthView
)

router = DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"discountcodes", DiscountCodeViewSet)
router.register(r"shoppingcarts", ShoppingCartViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('check-auth/', CheckAuthView.as_view(), name='check-auth'),
]
