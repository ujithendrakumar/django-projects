from django.contrib import admin
from django.urls import path,include
from basic_app import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include("basic_app.urls")),

]
