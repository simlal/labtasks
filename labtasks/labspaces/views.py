from django.shortcuts import render
from .models import Labspace

def your_labspaces(request):
    labspaces = Labspace.objects.all()
    context = {"labspaces": labspaces}

    return render(request, "labspaces/your_labspaces.html", context)

def labspace(request, pk):
    labspace = Labspace.objects.get(id=pk)
    
    context = {"labspace": labspace}
    return render(request, "labspaces/labspace.html", context)