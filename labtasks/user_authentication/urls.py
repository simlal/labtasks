from django.urls import path
from . import views

app_name = "user_authentication"

urlpatterns = [
    path("register", views.register_page, name="register_page"),
    path("success/<str:username>", views.successful_register, name="successful_register"),
    path("login", views.login_page, name="login_page"),
]
