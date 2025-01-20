from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'auth', views.AuthViewSet, basename='auth')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include(router.urls)),
] 