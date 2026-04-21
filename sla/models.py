from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class SLA(models.Model):
    STATUS_CHOICES = [
        ('ON_TRACK', 'On Track'),
        ('BREACHED', 'Breached'),
        ('EXCEEDED', 'Exceeded'),
    ]

    ticket = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ON_TRACK')

    def __str__(self):
        return f"{self.ticket} - {self.status}"
