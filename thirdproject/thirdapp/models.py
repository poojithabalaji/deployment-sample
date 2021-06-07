from django.db import models


# Create your models here.
class Users(models.Model):
    first_name =models.CharField(max_length=130)
    last_name =models.CharField(max_length=130)
    email =models.EmailField(max_length=230, unique=True)


# class formname(ModelForm):
#     class Meta:
#         model = Users
#         fields = ['first_name','last_name','email']
