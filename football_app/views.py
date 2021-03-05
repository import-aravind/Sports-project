from django.shortcuts import render
from django.http import HttpResponse
from football_app.forms import FormName
from django.shortcuts import render

# Create your views here.
def user_login(request):

    return render (request,'index.html')

def form_name_view(request):

    if request.method == "POST":
        form=FormName(request.POST)
        if form.is_valid():
            form.save()
    else:
        form= FormName()

    return render(request,'form_page.html',{'form':form})

def homepage(request):

    return render(request,'homepage.html')

def cricket(request):

    return render(request,'cricket.html')

def basketball(request):

    return render(request,'basketball.html')

def football(request):
    return render(request,'football.html')

def p1(request):
    return render(request,'p1.html')


def p2(request):
    return render(request,'p2.html')


def p3(request):
    return render(request,'p3.html')


def p4(request):
    return render(request,'p4.html')


def p5(request):
    return render(request,'p5.html')


def p6(request):
    return render(request,'p6.html')
