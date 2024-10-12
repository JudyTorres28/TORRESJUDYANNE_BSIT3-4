from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
   path('home/', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('login/', views.login_page, name='login'),
    
    
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/<int:pk>/', views.doctor_detail, name='doctor_detail'),
    path('doctors/new/', views.doctor_create, name='doctor_create'),
    path('doctors/<int:pk>/edit/', views.doctor_update, name='doctor_update'),
    path('doctors/<int:pk>/delete/', views.doctor_delete, name='doctor_delete'),
    
    
    ]   
