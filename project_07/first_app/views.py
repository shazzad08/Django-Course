from django.shortcuts import render,redirect
from .import models
# Create your views here.
def home(request):

    students = models.student.objects.all()
    print(students)
    return render(request,"home.html", {'data' : students})


def delete_record(request,roll):
    std = models.student.objects.get(pk = roll).delete()
    return redirect("homepage")