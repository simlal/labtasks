from django.urls import path
from . import views

app_name = "labspaces"

urlpatterns = [
    path("labspaces/", views.your_labspaces, name="your_labspaces"),
    path("labspaces/<str:pk>", views.labspace, name="labspace")
]
