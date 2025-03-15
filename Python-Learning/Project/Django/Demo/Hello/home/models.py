from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

# Contact here is a table which in simple terms we used in excel with columns and rows within the database.
# Make migrations creates changes and store it in a file.
# Migrate - Apply the pending the changes which created by makemigrations.
# Migrate apply would write into database in our case sqlite.(Changes will applied)  

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12)
    subject = models.CharField(max_length=122)
    message = models.TextField() 
    # attachement = models.FileField(upload_to='attachments/', blank=True, null=True)  
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Register(models.Model):
    username = models.CharField(max_length=122)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=122)
    date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'phone']

    def __str__(self):
        return self.username
    


