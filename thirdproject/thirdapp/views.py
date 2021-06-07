from django.shortcuts import render
from django.http import HttpResponse
from thirdapp.forms import formname


# Create your views here.
def index(request):
    return render(request, 'myhome.html')

def users(request):
    form =formname()
    if request.method =="POST":
        form =formname(request.POST)
        if form.is_valid():
            form.save(commit =True)

            return index(request)
        else:
            print("ERROR INVALID!!!!!")
    return render(request,'userpage.html',{"form":form})
