from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from .views import ItemCreateView, ItemUpdateView,ItemDeleteView,AntivirusCreateView,AntivirusDeleteView,AntivirusUpdateView


urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('sidebar/', views.sidebar, name='sidebar'),
    path('navbar/', views.navbar, name='navbar'),
    path('home', views.homepage , name='home'),
    # path('form/', views.employee_form, name='employee_form'),
    # path('item_form/', views.item_form, name='item_form'),
    path('antivirus_form/', AntivirusCreateView.as_view(), name='antivirus_form'),
    # path('<int:id>/', views.item_form, name='update'),
    # path('<int:id>/', views.employee_form, name='update'),
    path('delete/<int:id>/', views.employee_delete, name='delete'),
    # path('employee_list/',views.employee_list, name='employee_list'),
    path('list/',views.antivirus_list, name='antivirus_list'),
    path('item/new', ItemCreateView.as_view(), name='item_form'),
    path('entry/<int:pk>/update', AntivirusUpdateView.as_view(), name='update'),
    path('entry/<int:pk>/delete', AntivirusDeleteView.as_view(), name='delete'),

    path('', auth_views.LoginView.as_view(template_name='employee/login.html'), name='login'),
    path('register', views.register_request, name='register'),
    path("logout", views.logout_request, name= "logout"),

]

