from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def register_page(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # elminate casing duplaticates
            user.username = user.username.lower()
            user.save()
            login(request, user)
            context = {"user": user}
            return render(request, "user_authentication/successful_register.html", context)
    
    context = {
        "form": form
    }
    return render(request, "user_authentication/register.html", context)

def successful_register(request, username):
    user = User.objects.get(username=username)
    context = {"username": user}
    return render(request, "user_authentication/successful_register.html", context)

def login_page(request):
    # Redirect to index if already auth
    if request.user.is_authenticated:
        return redirect("base:index")
    
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        # Check for empty name or password
        if username == "":
            messages.error(request, "Enter a username")
            return render(request, "user_authentication/login.html")
        if password == "":
            messages.error(request, "Enter a password")
            return render(request, "user_authentication/login.html")
        
        
        # Check if user in db
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, f"User '{username}' does not exists.")
            user = False
        
        #Validate password
        valid_user = authenticate(request, username=username, password=password)

        # Login if valid
        if valid_user is not None:
            login(request, valid_user)
            return redirect("labspaces:your_labspaces")
        # user/pw error handling
        else :
            if user:
                messages.error(request, f"Invalid password for username for {username}")

        return render(request, "user_authentication/login.html")
    
    else:
        return render(request, "user_authentication/login.html")

def logout_user(request):
    logout(request)
    return redirect("base:index")