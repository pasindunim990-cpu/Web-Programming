from django.shortcuts import get_object_or_404, render
from .models import Student


def home(request):
    students = Student.objects.all().order_by("lastName", "firstName")
    return render(request, "home.html", {"students": students})


def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, "student_detail.html", {"student": student})
