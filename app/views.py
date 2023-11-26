from django.shortcuts import render

# Create your views here.
def free(request):
    return render(request,'free.html')
