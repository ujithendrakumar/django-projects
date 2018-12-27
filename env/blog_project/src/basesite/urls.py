from django.urls import path,include


from basesite import views
urlpatterns = [
        path("",views.index,name="index"),
]
