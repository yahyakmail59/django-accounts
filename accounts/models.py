from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    #image
    #age
    #job
    def __str__(self) -> str:
        return str(self.user)
