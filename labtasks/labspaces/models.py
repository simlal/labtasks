from django.db import models
from django.contrib.auth.models import User

class Labspace(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True, max_length=200)
    # participants =
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["updated", "created"]

    def __str__(self) -> str:
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    labspace = models.ForeignKey(Labspace, on_delete=models.CASCADE)
    body = models.TextField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.body[:50]

