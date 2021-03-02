from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage , name='home'),
    path('form/', views.employee_form, name='employee_form'),
    path('<int:id>/', views.employee_form, name='update'),
    path('delete/<int:id>/', views.employee_delete, name='delete'),
    path('employee_list/',views.employee_list, name='employee_list')
]

