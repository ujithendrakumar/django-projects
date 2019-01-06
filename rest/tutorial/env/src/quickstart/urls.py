from django.urls import path,include
from .models import Category
from rest_framework import routers
from quickstart import views
router = routers.DefaultRouter()
router.register('category', views.CategoryViewSet)


urlpatterns = [
    path('',include(router.urls