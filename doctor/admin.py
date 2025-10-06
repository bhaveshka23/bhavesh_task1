from django.contrib import admin
from .models import DoctorData ,BlogPost, Category


admin.site.register(DoctorData)
admin.site.register(BlogPost)
admin.site.register(Category)