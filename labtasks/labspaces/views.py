from django.shortcuts import render
from .models import Labspace, Message
from django.utils import timezone
from django.utils.timesince import timesince
# from django.contrib.auth.decorators import login_required

# @login_required
def your_labspaces(request):
    # Display your available labspaces
    labspaces = Labspace.objects.all()
    
    # Get timesince last message for each labspace
    timesince_last_message = {}

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
        "timesince_last_message": timesince_last_message
    }

    return render(request, "labspaces/your_labspaces.html", context)

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