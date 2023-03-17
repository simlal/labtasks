from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50, default="First Name")
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=2000)

    def __str__(self):
        return self.email
