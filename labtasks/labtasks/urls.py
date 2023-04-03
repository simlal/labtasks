from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("base.urls")),
    path("", include("contact_email.urls")),
    path("", include("user_authentication.urls"))
]
