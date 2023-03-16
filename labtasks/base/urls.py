from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("spaces/<str:pk>", views.spaces, name="spaces"),
    path("/register", views.register, name="register"),
    path("/login", views.login, name="login")
]