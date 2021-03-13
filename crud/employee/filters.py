import django_filters
from .models import *


class EmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = ['position','gender']
