from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import EmployeeForm,ItemForm, AntivirusForm, NewUserForm
from django.views.generic import ListView
from .models import Employee,Item, Antivirus
from .filters import EmployeeFilter
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.db.models import Q
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 





# Create your views here.

def sidebar(request):
    return render(request, 'employee/sidebar.html')


def navbar(request):
    return render(request, 'employee/navbar.html')


def homepage(request):
    females = Employee.objects.filter(gender='F')
    males = Employee.objects.filter(gender='M')
    employees = Employee.objects.all()
    total_employees = employees.count()
    total_females = females.count()
    total_males = males.count()
    context = {
        'total_employees': total_employees,
        'total_females': total_females,
        'total_males': total_males,
    }
    return render(request, 'employee/home.html', context)


def employee_list(request):
    employees = Employee.objects.all()
    myFilter = EmployeeFilter(request.GET, queryset=employees)
    employees = myFilter.qs
    context = {
        'employees': employees,
        'myFilter': myFilter,
    }
    return render(request, 'employee/employee_list.html', context)



def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('employee_list')



def item_list(request):
   
    items = Item.objects.filter(name__icontains=q)
    context={
        'items':items,
    }
    return render(request,'employee/item_list.html',context)

def employee_form(request, id=0):
   
   pass



class ItemCreateView( CreateView):
    model = Item
    template_name = 'employee/item_form.html'
    fields = ['name', 'item_type', 'acquisition_cost', 'source', 'item_properties', 'listing_platform','Date','listing_price','date_of_sale','sale_price','item_image']
    success_url = reverse_lazy('item_list')



class ItemUpdateView( UpdateView):
    model = Item
    template_name = 'employee/item_form.html'
    fields = ['name', 'item_type', 'acquisition_cost', 'source', 'item_properties', 'listing_platform','Date','listing_price','date_of_sale','sale_price','item_image']
    success_url = reverse_lazy('item_list')


class ItemDeleteView( DeleteView):
    model = Item
    template_name = 'employee/item_delete_confirm.html'
    success_url = reverse_lazy('item_list')


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
def item_form(request, id=0):
   
   pass



def antivirus_list(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    antivirus = Antivirus.objects.filter(
        Q(antivirus_id__icontains=q) |
        Q(officer_name__icontains=q) |
        Q(department__icontains=q)|
        Q(directorate__icontains=q)|
        Q(comp_serial_no__icontains=q) 
    )
    context = {
        'antivirus': antivirus
    }
    return render(request, 'employee/list.html', context)



class AntivirusCreateView( CreateView):
    model = Antivirus
    template_name = 'employee/antivirus_form.html'
    fields ='__all__'
    success_url = reverse_lazy('antivirus_list')


class AntivirusDeleteView( DeleteView):
    model = Antivirus
    template_name = 'employee/item_delete_confirm.html'
    success_url = reverse_lazy('antivirus_list')



class AntivirusUpdateView( UpdateView):
    model = Antivirus
    template_name = 'employee/antivirus_form.html'
    fields ='__all__'
    success_url = reverse_lazy('antivirus_list')




def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Registration failed..please read the instructions and try again..!!!")
	form = NewUserForm()
	return render (request=request, template_name="employee/register.html", context={"register_form":form})

def login_request(request):
    if request.method=="POST":
        form =AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {{username}}")
                return redirect('home')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
        context ={
            'login_form': form
        }
        form = AuthenticationForm()
        return render(request=request,template_name='employee/login.html',context=context)


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('login')