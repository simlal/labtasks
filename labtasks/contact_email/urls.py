from django.urls import path
from . import views

app_name = "contact_email"

urlpatterns = [
    path("header_error", views.header_error, name="header_error"),
]
