from django.urls import path
from basic_app import views
urlpatterns = [
    path('',views.index,name="name"),
    path('cbvpage',views.CBView.as_view(),name="cbvpage"),
    path('cbv',views.IndexView.as_view(),name="cbv"),

]
