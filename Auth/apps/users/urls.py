from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.registration, name='register'),
    path('http404/', views.http404, name='http404'),
    path('', views.main, name='main')
]