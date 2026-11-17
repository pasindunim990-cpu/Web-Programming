from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils.http import urlencode
from .models import Student, Module


def studentlist(request, page=1):
    students = Student.objects.all().order_by("lastName", "firstName")
    paginator = Paginator(students, 10)
    page_obj = paginator.get_page(page)
    query_string = urlencode(request.GET.copy())
    return render(request, "studentlist.html", {
        "page_obj": page_obj,
        "query_string": query_string,
    })


def modulelist(request):
    modules = Module.objects.all().order_by("code")
    return render(request, "modulelist.html", {"modules": modules})
