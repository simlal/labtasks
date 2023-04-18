from django.shortcuts import render, redirect

from .models import Labspace, Message
from .forms import LabspaceForm, editLabspaceForm

from django.utils import timezone
from django.utils.timesince import timesince
from django.contrib.auth.decorators import login_required

@login_required(login_url="user_authentication:login_page")
def your_labspaces(request):
    
    # Create a new labspace based on form
    if request.method == "POST":
        form = LabspaceForm(request.POST)
        if form.is_valid():
            labspace = form.save(commit=False)
            labspace.host = request.user
            labspace.save()
            return redirect("labspaces:your_labspaces")

    # Display  available labspaces and create labspace form
    else: 
        form = LabspaceForm()    # To render the form on request.get
        
        labspaces = Labspace.objects.all().order_by('-pinned', '-updated', '-created')    # Get all available labspaces
        
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

        context = {
            "labspaces": labspaces,
            "timesince_last_message": timesince_last_message,
            "form": form
        }

        return render(request, "labspaces/your_labspaces.html", context)

@login_required(login_url="user_authentication:login_page")
def edit_labspace(request, pk):
    
    # Get selected labspace
    labspace = Labspace.objects.get(id=pk)

    # Validate if current user is the host
    if request.user != labspace.host and not request.user.is_superuser:
        return redirect("labspaces:unauthorized") 
    
    if request.method == 'POST':
        # Edit db to change name + description
        form = editLabspaceForm(request.POST, instance=labspace)
        if form.is_valid():
            if form.has_changed():
                
                # Update only changed fields
                for field in form.changed_data:
                    setattr(labspace, field, form.cleaned_data[field])
                labspace.save()
            return redirect("labspaces:your_labspaces")
    else:
        form = editLabspaceForm(instance=labspace)

    context = {
        "labspace": labspace,
        "form": form
    }
    return render(request, "labspaces/edit_labspace.html", context)

@login_required(login_url="user_authentication:login_page")
def delete_labspace(request, pk):
    
    # Get selected labspace
    labspace = Labspace.objects.get(id=pk)

    # Validate if current user is the host
    if request.user != labspace.host and not request.user.is_superuser:
        return redirect("labspaces:unauthorized") 

    # Delete labspace
    if request.method == "POST":
        
        # Get the labspace obj with the given pj
        labspace_to_del = Labspace.objects.get(id=pk)
        
        # Delete the labspace
        labspace_to_del.delete()
        
        # Redirect to success delete
        return render(request, "labspaces/success_delete.html")
    
    # Get request
    else:
        # Get the labspace obj
        labspace = Labspace.objects.get(id=pk)
        # Find last message if possible
        try : 
                last_message = Message.objects.filter(labspace=labspace.id).latest("created")
        except Exception as e:
                print(e)
                last_message = False
            
        # Save latest message based on space id
        if last_message:
            timesince_last = timesince(last_message.created, timezone.now())
        else:
            timesince_last = "No messages yet!"
        
        context = {
            "labspace": labspace,
            "last_message": last_message,
            "timesince_last": timesince_last
        }
    return render(request, "labspaces/delete_labspace.html", context)

def cancel_delete_labspace(request):
    return redirect("labspaces:your_labspaces")

def cancel_edit_labspace():
    return redirect("labspaces:your_labspaces")

def unauthorized(request):
    return render(request, "labspaces/unauthorized.html")

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