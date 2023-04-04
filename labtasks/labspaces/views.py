from django.shortcuts import render
from .models import Labspace, Message
from django.contrib.auth.decorators import login_required

@login_required
def your_labspaces(request):
    # Display your available labspaces
    labspaces = Labspace.objects.all()
    context = {"labspaces": labspaces}

    return render(request, "labspaces/your_labspaces.html", context)

@login_required
def labspace(request, pk):
    # Get labspace and all related messages
    labspace = Labspace.objects.get(id=pk)
    messages = Message.objects.filter(labspace=labspace)
    
    context = {
        "labspace": labspace,
        "messages": messages,
        "current_user": request.user
    }

    return render(request, "labspaces/labspace.html", context)