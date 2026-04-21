from django.db import models

class Request(models.Model):
    requester_name = models.CharField(max_length=100)
    request_type = models.CharField(max_length=50)
    description = models.TextField()
    requested_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"{self.request_type} by {self.requester_name}"
