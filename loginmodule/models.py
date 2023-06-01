from django.db import models
from django.utils import timezone
# Create your models here.
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    message = models.CharField(max_length=500, default="")
    timestamp = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
