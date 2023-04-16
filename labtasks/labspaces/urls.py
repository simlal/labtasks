from django.urls import path
from . import views

app_name = "labspaces"

urlpatterns = [
    path("labspaces/", views.your_labspaces, name="your_labspaces"),
    path("labspaces/<str:pk>", views.labspace, name="labspace"),
    path("labspaces/<str:pk>/edit", views.edit_labspace, name="edit_labspace"),
    path("labspaces/<str:pk>/delete", views.delete_labspace, name="delete_labspace"),
    path("labspaces/", views.cancel_delete_labspace, name="cancel_delete_labspace")
]
