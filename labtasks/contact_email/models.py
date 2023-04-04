from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=2000)
    send_date = models.DateField()

    def __str__(self):
        return f"Message from {self.email} (sent on {self.send_date})"
