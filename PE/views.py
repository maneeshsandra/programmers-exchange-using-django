from django.shortcuts import render
from django.http import HttpResponse
from PE.models import Problem,Contact
from . import models
from django.views import generic


# Create your views here.
def home(request):
    return render(request,'index.html')

def get_absolute_url(self):
    return f"/{self}"

class Easy(generic.ListView):
    template_name='easy.html'

    def get_queryset(self):
        return Problem.objects.filter(difficulty='easy')

class Medium(generic.ListView):
    template_name='medium.html'

    def get_queryset(self):
        return Problem.objects.filter(difficulty='medium')

class Hard(generic.ListView):
    template_name='hard.html'

    def get_queryset(self):
        return Problem.objects.filter(difficulty='hard')

class DetailView(generic.DetailView):
    model=Problem
    template_name='detail.html'

def contribute(request):
    return render(request,'contribute.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')
def detail(request):
    return HttpResponse("hi")


def problems(request):
    
    name=request.POST['name']
    title=request.POST['title']
    difficulty=request.POST['example']
    description=request.POST['description']
    solution=request.POST['solution']
    code=request.POST['code']

    question=Problem(name=name,title=title,difficulty=difficulty,description=description,solution=solution,code=code)
    question.save()
    return render(request,'thanks.html')

def action(request):
    firstname=request.POST['name']
    email=request.POST['email']
    mobile=request.POST['mobile']
    message=request.POST['message']

    data=Contact(firstname=firstname,email=email,mobile=mobile,message=message)
    data.save()

    return render(request,'thanking.html',{'firstname':firstname})


