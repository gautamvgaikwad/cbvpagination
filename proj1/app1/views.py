from django.shortcuts import render
from .models import Employee
from django.views.generic import ListView


# Create your views here.
class EmpListView(ListView):
    model=Employee
    template_name='emp_list.html'
    context_object_name='emp1'
    paginate_by=4
    queryset=Employee.objects.all()