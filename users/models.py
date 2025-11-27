from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from .managers import CoustomUserManager

class User(AbstractUser):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email= models.EmailField(unique=True,)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    USERNAME_FIELD= "email"
    REQUIRED_FIELDS=[]
    objects= CoustomUserManager()

    def __str__(self):
        return self.email    
