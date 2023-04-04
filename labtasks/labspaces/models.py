from django.db import models

class Labspace(models.Model):
    # host
    # topic
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants =
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
