from django.urls import path
from todo import views as todo_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',todo_views.index,name="index"),
    path('about',todo_views.about,name="about"),
    path('add',todo_views.add,name="add"),
    path('complete/<todo_id>',todo_views.complete, name="complete"),
    path('delete_completed',todo_views.completeDelete, name="delete_completed"),
    path('delete_all',todo_views.completeAll, name="delete_all"),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view()),
    path('signup/', todo_views.signup,name="signup"),
]