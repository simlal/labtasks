from django.shortcuts import render, redirect

from .models import Labspace, Message
from .forms import LabspaceForm

from django.utils import timezone
from django.utils.timesince import timesince
# from django.contrib.auth.decorators import login_required

# @login_required
def your_labspaces(request):
    
    # Create a new labspace based on form
    if request.method == "POST":
        form = LabspaceForm(request.POST)
        if form.is_valid():
            form.save()
            context = {"form": form}
            return redirect("labspaces:your_labspaces")

    # Display  available labspaces and create labspace form
    else: 
        form = LabspaceForm()    # To render the form on request.get
        
        labspaces = Labspace.objects.all()    # Get all available labspaces
        
        timesince_last_message = {}    # Initialize timesince dict

        # Handle the empty queryset
        for labspace in labspaces:
            try : 
                last_message = Message.objects.filter(labspace=labspace.id).latest("created")
            except Exception as e:
                print(e)
                last_message = False
            
            # Save latest message based on space id
            if last_message:
                timesince_last_message[labspace.id] = timesince(last_message.created, timezone.now())
            else:
                timesince_last_message[labspace.id] = 'No messages yet'

        print(timesince_last_message)        
        
        context = {
            "labspaces": labspaces,
            "timesince_last_message": timesince_last_message,
            "form": form
        }

        return render(request, "labspaces/your_labspaces.html", context)

def edit_labspace(request, pk):
    labspace = Labspace.objects.get(id=pk)
    context = {"labspace": labspace}
    return render(request, "labspaces/edit_labspace.html", context)

def delete_labspace(request, pk):
    labspace = Labspace.objects.get(id=pk)
    context = {"labspace": labspace}
    return render(request, "labspaces/delete_labspace.html")

# @login_required
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