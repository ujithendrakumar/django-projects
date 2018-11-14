from django.urls import path
from helloworld import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('getin', views.getin, name='getin'),
    path('userregister', views.userregister, name='reg'),
    path('delete/<name_id>', views.delete, name='delete'),
    path('update/<name_id>', views.update, name='update'),
    path('blog', views.blog, name='blog'),
    path('blog_details/<blog_id>', views.blog_details, name='details'),
    
]
