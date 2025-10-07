from django.db import models
from django.contrib.auth.models import User

class DoctorData(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    profile_pic = models.ImageField(upload_to = "profile_pics/" , blank = True, null = True)
    line1 = models.CharField(max_length = 300 , blank = True , null = True)
    city = models.CharField(max_length = 50 , blank = True , null = True)
    state = models.CharField(max_length = 50 , blank = True , null = True)
    pincode = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    category = models.CharField(max_length = 100, unique = True)

    def __str__(self):
        return self.category


class BlogPost(models.Model):
    author = models.ForeignKey(User , on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    summary = models.TextField()
    content = models.TextField()
    is_draft = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title