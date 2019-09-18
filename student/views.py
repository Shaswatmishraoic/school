from django.shortcuts import render
from django.http import HttpResponse
from .models import stud

def index(request):
  students = stud.objects.all()
  context={'students':students}
  return render(request,'index.html',context)
def details(request):
  if request.method =='POST':
    name= request.POST.get("name")
    roll= request.POST.get("roll")
    sem = request.POST.get("sem")
    s=stud(naam=name, roll=int(roll), sem=int(sem))
    try:
      s.save()
    except:
      return HttpResponse('roll no. exist')
    return HttpResponse("YOUR NAME IS SAVE")
  else:
    return render(request,'cr.html')