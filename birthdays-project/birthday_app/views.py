from django.shortcuts import render
from django.http import Http404

from .models import Employee


def index(request):
    employee_queryset = Employee.objects.all()
    return render(request, 'employees/index.html', {
        'Employee': employee_queryset,
    })


def employee_detail(request, id):
    try:
        employee_queryset = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        raise Http404('No such employee.')
    return render(request, 'employees/employee_detail.html', {
        'Employee': employee_queryset,
    })
