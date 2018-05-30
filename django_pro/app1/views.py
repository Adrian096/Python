from django.shortcuts import render
from django . http import HttpResponse
from .models import Student

# Create your views here.
def index ( request ):
    model = Student.objects.all()
    
    
    p1 = request.GET.get("imie")
    p2 = request.GET.get("nazwisko")
    p3 = request.GET.get("nr")
    
    
    student = Student(imie=p1, nazwisko=p2, nr_albumu=p3)
    student.save()
    
    return render(request, 'app1/index.html', {'students': model})
