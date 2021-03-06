from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('sidebar/', views.sidebar, name='sidebar'),
    path('navbar/', views.navbar, name='navbar'),
    path('', views.homepage , name='home'),
    path('form/', views.employee_form, name='employee_form'),
    path('<int:id>/', views.employee_form, name='update'),
    path('delete/<int:id>/', views.employee_delete, name='delete'),
    path('employee_list/',views.employee_list, name='employee_list'),
    path('login/', auth_views.LoginView.as_view(template_name='employee/login.html'), name='login'),
    path('register/', views.user_register, name='register')
]

