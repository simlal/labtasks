from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=2000)
    send_date = models.DateField()
