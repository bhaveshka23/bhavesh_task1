from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PatientData(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    profile_pic = models.ImageField(upload_to = "profile_pics/" , blank = True, null = True)
    line1 = models.CharField(max_length = 300 , blank = True , null = True)
    city = models.CharField(max_length = 50 , blank = True , null = True)
    state = models.CharField(max_length = 50 , blank = True , null = True)
    pincode = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username
