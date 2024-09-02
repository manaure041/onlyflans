from email import message
from ipaddress import ip_address
import uuid
from django.db import models
from django.utils import timezone

# Create your models here.

class Flan(models.Model):
    flan_uuid=models.UUIDField()
    name= models.CharField(max_length=64)
    
    description=models.TextField(default='')
    image_url=models.URLField(default='')
    slug=models.SlugField(default='')
    is_private=models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} ({self.id})"
    
    
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
    submission_date = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    def __str__(self):
        return f"Nombre: {self.customer_name}, Email: {self.customer_email}"
    
    
class Pasteles(models.Model):
    flan_uuid=models.UUIDField()
    name= models.CharField(max_length=64)
    
    description=models.TextField(default='')
    image_url=models.URLField(default='')
    slug=models.SlugField(default='')
    is_private=models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} ({self.id})"
   
   

    