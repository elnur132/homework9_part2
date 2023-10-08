from django.shortcuts import render, redirect
from .models import Names

# Create your views here.
def default_name(request):
    names = Names.objects.all()
    return render(request, 'names.html', {'names': names}) 

def add_name(request):
    if request.method == "POST":
        at = request.POST
        add = Names.objects.create(name=at['name'])
        add.save()
        return redirect('default_name')
    else:
        return render(request, 'add_name.html')