from django.urls import path
from basic_app import views

app_name = "basic_app"

urlpatterns = [
    path('',views.index,name="name"),
    path('cbvpage',views.CBView.as_view(),name="cbvpage"),
    path('cbv',views.IndexView.as_view(),name="cbv"),
    path('schools',views.SchoolListView.as_view(),name="schools"),
    path('<pk>',views.SchoolDetailView.as_view(),name="detail"),


]
