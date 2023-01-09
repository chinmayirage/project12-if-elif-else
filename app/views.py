from django.shortcuts import render

# Create your views here.
def oper(request):
    d={'a':100,'b':400}
    return render (request,'oper.html',d)