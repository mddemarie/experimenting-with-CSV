from django.db import models

class Device(models.Model):
    TYPE_CHOICES = [
        (1, 'sensor'),
        (2, 'gateway')
    ]
    STATUS_CHOICES = [
        (1, 'online'),
        (2, 'offline')
    ]

    device_id = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    device_type = models.CharField(choices=TYPE_CHOICES, max_length=1)
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
